"""Apply the preregistered decision rules to follow-up test results.

Usage (from the repository root):

    python3 protocols/analyze.py RESULTS.csv     # evaluate real results
    python3 protocols/analyze.py --selftest      # check the pipeline on synthetic data

RESULTS.csv has one row per mission, with columns

    study, seed, arm, round, test_solve_pct

where `study` is T1, T2 or T3, `arm` is one of the arms registered for that
study in protocols/PREREGISTRATION.md, and `round` is the checkpoint round.
Seeds must lie in the registered confirmatory range, and every seed must have
every arm, or the script refuses to evaluate. The rules are fixed in
PREREGISTRATION.md; this script only applies them.
"""
import csv
import random
import sys
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "data"))
from frmstats import bootstrap_ci, mean, signs, wilcoxon_upper  # noqa: E402

# Registered designs (keep in sync with PREREGISTRATION.md).
STUDIES = {
    "T1": {"seeds": range(8601, 8625), "final": 32,
           "arms": ("LOOP", "RS", "ES"),
           "contrasts": [("T1-P", "LOOP", "RS", 0.01, "primary"),
                         ("T1-S", "LOOP", "ES", 0.01, "secondary")]},
    "T2": {"seeds": range(8701, 8725), "final": 32,
           "arms": ("BEST", "DEFAULT"),
           "contrasts": [("T2-P", "BEST", "DEFAULT", None, "estimate")]},
    "T3": {"seeds": range(8901, 8949), "final": 128,
           "arms": ("C6", "C6F", "C6R"),
           "contrasts": [("T3-P", "C6", "C6F", 0.01, "primary"),
                         ("T3-S", "C6", "C6R", 0.05, "secondary")]},
}
FLOOR = 0.5   # observed mean must reach half the effect the study is powered for
BAR = 1.0     # the smallest effect of interest (pp)


def load(path):
    data = defaultdict(dict)  # (study, round) -> {(seed, arm): value}
    with open(path, newline="") as f:
        for r in csv.DictReader(f):
            key = (r["study"].strip(), int(r["round"]))
            data[key][(int(r["seed"]), r["arm"].strip().upper())] = float(r["test_solve_pct"])
    return data


def evaluate(data, label="", verdicts=None):
    failures = 0
    verdicts = {} if verdicts is None else verdicts
    for study, spec in STUDIES.items():
        cells = data.get((study, spec["final"]))
        if not cells:
            print(f"{study}: no results at round {spec['final']}; not evaluated")
            continue
        seeds = sorted({s for s, _ in cells})
        bad = [s for s in seeds if s not in spec["seeds"]]
        missing = [(s, a) for s in spec["seeds"] for a in spec["arms"] if (s, a) not in cells]
        if bad or missing:
            print(f"{study}: REFUSED. Seeds outside the registered range: {bad[:5]}; "
                  f"missing seed/arm pairs: {missing[:5]}{' ...' if len(missing) > 5 else ''}")
            failures += 1
            continue
        print(f"{study} (round {spec['final']}, n = {len(spec['seeds'])} seeds){label}")
        for name, a, b, alpha, role in spec["contrasts"]:
            d = [cells[(s, a)] - cells[(s, b)] for s in spec["seeds"]]
            m, (lo, hi) = mean(d), bootstrap_ci(d)
            up, down, zero = signs(d)
            line = f"  {name} {a} - {b}: mean {m:+.2f} pp, 95% CI [{lo:+.2f}, {hi:+.2f}], seeds +/-/0 {up}/{down}/{zero}"
            if alpha is None:
                verdict = ("BOUNDED: even the best fixed Imp is worth < +1.0 pp" if hi < BAR else
                           "HEADROOM: the best fixed Imp may be worth >= +1.0 pp")
                print(f"{line}\n    -> {verdict}")
                verdicts[name] = verdict.split(":")[0]
                continue
            p = wilcoxon_upper(d)
            ok = p < alpha and m >= FLOOR
            verdicts[name] = "PASS" if ok else "FAIL"
            print(f"{line}, one-sided exact Wilcoxon p = {p:.3g}\n"
                  f"    -> {role}: {'PASS' if ok else 'FAIL'} (rule: p < {alpha} and mean >= +{FLOOR} pp)")
    return failures


def selftest():
    """Synthetic data with known effects; checks the plumbing, not the module."""
    rng = random.Random(0)
    rows = []
    effects = {"T1": {"LOOP": 3.0, "RS": 0.0, "ES": 2.9},
               "T2": {"BEST": 0.2, "DEFAULT": 0.0},
               "T3": {"C6": 0.0, "C6F": 0.0, "C6R": 0.0}}
    for study, spec in STUDIES.items():
        for s in spec["seeds"]:
            base = rng.gauss(40, 2)
            for arm in spec["arms"]:
                rows.append((study, s, arm, spec["final"],
                             round(base + effects[study][arm] + rng.gauss(0, 0.5), 1)))
    data = defaultdict(dict)
    for study, s, arm, rnd, v in rows:
        data[(study, rnd)][(s, arm)] = v
    print("SELF-TEST ON SYNTHETIC DATA. These numbers are not results.\n")
    got = {}
    evaluate(data, label=" [synthetic]", verdicts=got)
    want = {"T1-P": "PASS", "T1-S": "FAIL", "T2-P": "BOUNDED", "T3-P": "FAIL", "T3-S": "FAIL"}
    assert got == want, (got, want)
    # Refusal check: drop one cell and confirm the study is not evaluated.
    del data[("T3", 128)][(8901, "C6")]
    print()
    assert evaluate({("T3", 128): data[("T3", 128)]}) == 1
    print("\nSelf-test passed: every verdict matched the effect built into the synthetic data,\n"
          "and incomplete data was refused.")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit(__doc__)
    if sys.argv[1] == "--selftest":
        selftest()
    else:
        sys.exit(1 if evaluate(load(sys.argv[1])) else 0)
