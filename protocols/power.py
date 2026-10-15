"""Power analysis for the follow-up tests, from the Stage 3 per-seed data.

Run from the repository root:  python3 protocols/power.py

The noise model is the empirical distribution of the 24 Stage 3 B-1
differences (C6 − C6f at round 32, data/felix-c3_per_seed_test_solve.csv),
centred to mean zero and shifted to each assumed true effect. Each simulated
study draws n seeds with replacement and applies the one-sided exact Wilcoxon
test at alpha = 0.01, under two decision rules:

  p-only : one-sided p < 0.01
  joint  : one-sided p < 0.01 AND observed mean >= +1.0 pp (the rule Stage 3 used)
  floor  : one-sided p < 0.01 AND observed mean >= +0.5 pp (the rule proposed in
           protocols/PREREGISTRATION.md: significance, plus a floor at half the
           effect the study is powered for)

The joint rule caps power near 57% when the true effect equals the +1.0 pp
bar, because the observed mean falls below the bar about half the time, and
more seeds cannot fix that.
"""
import csv
import random
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "data"))
from frmstats import mean, wilcoxon_upper  # noqa: E402

import numpy as np  # noqa: E402


def wilcoxon_upper_fast(d):
    """Same exact test as frmstats.wilcoxon_upper, vectorised for simulation."""
    d = np.asarray([x for x in d if x != 0])
    n = len(d)
    a = np.abs(d)
    order = np.argsort(a, kind="stable")
    sa = a[order]
    ranks2 = np.empty(n, dtype=np.int64)
    i = 0
    while i < n:
        j = i
        while j + 1 < n and sa[j + 1] == sa[i]:
            j += 1
        ranks2[order[i:j + 1]] = i + j + 2
        i = j + 1
    w_obs = int(ranks2[d > 0].sum())
    dist = np.zeros(int(ranks2.sum()) + 1)
    dist[0] = 1.0
    for r in ranks2:
        shifted = np.zeros_like(dist)
        shifted[r:] = dist[:-r]
        dist = 0.5 * (dist + shifted)
    return float(dist[w_obs:].sum())

with open(ROOT / "data" / "felix-c3_per_seed_test_solve.csv", newline="") as f:
    rows = list(csv.DictReader(f))
b1 = [float(r["c6_r32_pct"]) - float(r["c6f_r32_pct"]) for r in rows]
m = mean(b1)
sd = (sum((x - m) ** 2 for x in b1) / (len(b1) - 1)) ** 0.5
centred = [x - m for x in b1]

SIMS = 2000
ALPHA = 0.01
BAR = 1.0
FLOOR = 0.5


def power(n, effect, rng):
    p_only = joint = floor = 0
    for _ in range(SIMS):
        d = [rng.choice(centred) + effect for _ in range(n)]
        # The printed per-seed values are rounded to 0.1 pp; keep that grain so
        # ties and zeros behave as they would in real data.
        d = [round(x, 1) for x in d]
        if wilcoxon_upper_fast(d) < ALPHA:
            p_only += 1
            joint += mean(d) >= BAR
            floor += mean(d) >= FLOOR
    return p_only / SIMS, joint / SIMS, floor / SIMS


if __name__ == "__main__":
    check = random.Random(1)
    for _ in range(200):  # the fast test must agree with the reference test
        d = [round(check.choice(centred) + check.uniform(-1, 2), 1) for _ in range(check.randint(8, 40))]
        assert abs(wilcoxon_upper_fast(d) - wilcoxon_upper(d)) < 1e-9, d
    print(f"B-1 noise model: n = {len(b1)}, mean {m:+.3f} pp, SD {sd:.3f} pp")
    print(f"{SIMS} simulated studies per cell, one-sided exact Wilcoxon, alpha = {ALPHA}\n")
    print(f"{'seeds':>6} {'true effect':>12} {'p-only':>8} {'joint':>8} {'floor':>8}")
    rng = random.Random(20261015)
    for effect in (0.5, 1.0, 1.5, 2.0):
        for n in (24, 32, 48, 64, 96):
            po, jo, fl = power(n, effect, rng)
            print(f"{n:>6} {effect:>+11.1f}  {po:>8.2f} {jo:>8.2f} {fl:>8.2f}")
        print()
