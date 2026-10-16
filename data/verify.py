"""Recompute the papers' headline statistics from the per-seed CSV files.

Uses only the Python standard library. Run from the repository root:

    python3 data/verify.py

The exact Wilcoxon signed-rank test follows Appendix C of the FELIX-C3 paper:
zero differences are dropped, tied absolute differences get midranks, and the
null distribution of the doubled signed-rank statistic is computed exactly.

The per-seed values in the papers are printed rounded (C3 test solve rates to
0.1 percentage points; C9 rates and C7 and C9 bug counts to 0.01), so recomputed
means may differ
from the reported ones in the last printed digit, and p-values from rounded
inputs are compared within a tolerance.
"""
import csv
import math
import sys
from pathlib import Path

DATA = Path(__file__).resolve().parent
sys.path.insert(0, str(DATA))
from frmstats import mean, signs, wilcoxon_two_sided, wilcoxon_upper  # noqa: E402
failures = 0


def load(name):
    with open(DATA / name, newline="") as f:
        return list(csv.DictReader(f))


def col(rows, key):
    return [float(r[key]) for r in rows]


def check(label, got, want, tol):
    global failures
    ok = abs(got - want) <= tol
    failures += not ok
    print(f"  {'ok  ' if ok else 'FAIL'} {label}: recomputed {got:.4g}, reported {want:g}")


def check_p(label, got, want):
    """p-values from rounded inputs: pass if within a factor of 2 (log scale)."""
    global failures
    ok = abs(math.log10(got) - math.log10(want)) <= math.log10(2)
    failures += not ok
    print(f"  {'ok  ' if ok else 'FAIL'} {label}: recomputed p = {got:.3g}, reported p = {want:g}")


def check_eq(label, got, want):
    global failures
    ok = got == want
    failures += not ok
    print(f"  {'ok  ' if ok else 'FAIL'} {label}: recomputed {got}, reported {want}")


# FELIX-C3, Table 24 (confirmatory, seeds 7101-7124) -------------------------
print("FELIX-C3 confirmatory (Table 24)")
c3 = load("felix-c3_per_seed_test_solve.csv")
check_eq("seeds", len(c3), 24)
for key, want in [("r0_pct", 27.4), ("c6_r16_pct", 38.0), ("c6_r32_pct", 40.1),
                  ("c6f_r16_pct", 38.0), ("c6f_r32_pct", 39.8),
                  ("c6r_r16_pct", 38.3), ("c6r_r32_pct", 39.4)]:
    check(f"mean {key}", mean(col(c3, key)), want, 0.051)
trials, adopted, meta = (col(c3, k) for k in
                         ("c6_imp_trials", "c6_imp_adopted", "c6_imp_adopted_meta"))
check_eq("Imp trials (total)", int(sum(trials)), 166)
check_eq("adopted Imp edits (total)", int(sum(adopted)), 60)
check_eq("adopted edits that changed the editing procedure", int(sum(meta)), 25)
check_eq("A-2 missions adopting an edit", sum(a > 0 for a in adopted), 21)
check_eq("A-3 missions whose editing procedure changed", sum(m > 0 for m in meta), 17)

a4 = [b - a for a, b in zip(col(c3, "c6_r16_pct"), col(c3, "c6_r32_pct"))]
check("A-4 mean second-half progress (pp)", mean(a4), 2.12, 0.051)
check_eq("A-4 seeds up/down/unchanged", signs(a4), (18, 2, 4))
check_p("A-4 one-sided Wilcoxon", wilcoxon_upper(a4), 7.6e-6)

b1 = [a - b for a, b in zip(col(c3, "c6_r32_pct"), col(c3, "c6f_r32_pct"))]
check("B-1 mean C6 - C6f (pp)", mean(b1), 0.35, 0.051)
check_eq("B-1 seeds +/-/0", signs(b1), (14, 10, 0))
check_p("B-1 one-sided Wilcoxon", wilcoxon_upper(b1), 0.23)

b2 = [a - b for a, b in zip(col(c3, "c6_r32_pct"), col(c3, "c6r_r32_pct"))]
check("B-2 mean C6 - C6r (pp)", mean(b2), 0.72, 0.051)
check_eq("B-2 seeds +/-/0", signs(b2), (15, 8, 1))
check_p("B-2 one-sided Wilcoxon", wilcoxon_upper(b2), 0.079)

# FELIX-C3, Table 10 (Gate 1 pilot, seeds 3201-3208) -------------------------
print("FELIX-C3 Gate 1 pilot (Table 10)")
g1 = load("felix-c3_gate1_pilot.csv")
check_eq("seeds", len(g1), 8)
for key, want in [("c6_r0", 0.266), ("c6_r16", 0.384), ("c6_r32", 0.406),
                  ("c6f_r32", 0.405), ("c6r_r32", 0.408)]:
    check(f"mean {key}", mean(col(g1, key)), want, 0.00051)

# FELIX-C7, Table 7 (seeds 7101-7124) -----------------------------------------
print("FELIX-C7 transfer to real bugs (Table 7)")
c7 = load("felix-c7_per_seed_bugs_solved.csv")
check_eq("seeds", len(c7), 24)
for key, want in [("r0", 20.96), ("c6", 25.81), ("c6f", 25.55), ("c6r", 26.48),
                  ("c6_permuted", 19.84), ("r0_b48", 34.37), ("c6_b48", 36.54),
                  ("delta_p1", 4.85)]:
    check(f"mean {key}", mean(col(c7, key)), want, 0.011)


def diff(rows, a, b):
    return [x - y for x, y in zip(col(rows, a), col(rows, b))]


p1 = diff(c7, "c6", "r0")
check("P1 delta column equals c6 - r0 (max abs gap)",
      max(abs(x - y) for x, y in zip(p1, col(c7, "delta_p1"))), 0.0, 0.011)
for label, d, want_signs, want_p, sided in [
        ("P1 C6 - r0", p1, (23, 1, 0), 3.0e-7, 1),
        ("S1 C6f - r0", diff(c7, "c6f", "r0"), (23, 0, 1), 1.2e-7, 1),
        ("S1 C6r - r0", diff(c7, "c6r", "r0"), (23, 1, 0), 1.2e-7, 1),
        ("S2 C6 - C6f", diff(c7, "c6", "c6f"), (12, 11, 1), 0.68, 2),
        ("S2 C6 - C6r", diff(c7, "c6", "c6r"), (10, 14, 0), 0.35, 2),
        ("S4 budget 48, C6 - r0", diff(c7, "c6_b48", "r0_b48"), (19, 5, 0), 4.3e-4, 1),
        ("S5 C6 - permuted", diff(c7, "c6", "c6_permuted"), (22, 2, 0), 3.0e-7, 1)]:
    check_eq(f"{label} seeds +/-/0", signs([round(x, 6) for x in d]), want_signs)
    p = wilcoxon_upper(d) if sided == 1 else wilcoxon_two_sided(d)
    check_p(f"{label} {'one' if sided == 1 else 'two'}-sided Wilcoxon", p, want_p)

# FELIX-C9, Table 11 (confirmatory, seeds 7901-7924) --------------------------
print("FELIX-C9 structural self-modification (Table 11)")
c9 = load("felix-c9_per_seed.csv")
check_eq("seeds", len(c9), 24)
check_eq("campaign = seed index mod 2", [int(r["campaign"]) for r in c9], [i % 2 for i in range(24)])
for key, want in [("e_r32_pct", 43.03), ("d_r32_pct", 40.47), ("r_r32_pct", 39.52), ("t_r32_pct", 46.15),
                  ("bugs_e", 25.36), ("bugs_d", 24.97), ("bugs_r0", 20.74)]:
    check(f"mean {key}", mean(col(c9, key)), want, 0.011)
check("E - D column equals e - d (max abs gap)",
      max(abs(x - y) for x, y in zip(diff(c9, "e_r32_pct", "d_r32_pct"), col(c9, "e_minus_d_pp"))), 0.0, 0.011)
c9_0 = [r for r in c9 if r["campaign"] == "0"]
c9_1 = [r for r in c9 if r["campaign"] == "1"]
check_eq("campaign 0: E identical to T on every seed",
         all(r["e_r32_pct"] == r["t_r32_pct"] for r in c9_0), True)
for label, d, want_mean, want_signs, want_p, sided in [
        ("B-1 E - D", diff(c9, "e_r32_pct", "d_r32_pct"), 2.57, (18, 6, 0), 0.0028, 1),
        ("B-2 E - R", diff(c9, "e_r32_pct", "r_r32_pct"), 3.52, (15, 7, 2), 0.0011, 1),
        ("T - D", diff(c9, "t_r32_pct", "d_r32_pct"), 5.68, (22, 2, 0), 3e-7, 1),
        ("E - D, campaign 0", diff(c9_0, "e_r32_pct", "d_r32_pct"), 5.70, (12, 0, 0), 0.0002, 1),
        ("E - D, campaign 1", diff(c9_1, "e_r32_pct", "d_r32_pct"), -0.57, (6, 6, 0), 0.66, 1),
        ("E - T", diff(c9, "e_r32_pct", "t_r32_pct"), -3.11, (1, 11, 12), 0.001, 2),
        ("R - D", diff(c9, "r_r32_pct", "d_r32_pct"), -0.95, (8, 14, 2), 0.049, 2),
        ("S-3 bugs E - D", diff(c9, "bugs_e", "bugs_d"), 0.39, (13, 11, 0), 0.52, 2),
        ("S-3 bugs E - r0", diff(c9, "bugs_e", "bugs_r0"), 4.62, (24, 0, 0), 6e-8, 1),
        ("S-3 bugs D - r0", diff(c9, "bugs_d", "bugs_r0"), 4.23, (23, 1, 0), 1e-7, 1)]:
    check(f"{label} mean", mean(d), want_mean, 0.011)
    check_eq(f"{label} seeds +/-/0", signs([round(x, 6) for x in d]), want_signs)
    p = wilcoxon_upper(d) if sided == 1 else wilcoxon_two_sided(d)
    check_p(f"{label} {'one' if sided == 1 else 'two'}-sided Wilcoxon", p, want_p)

# FELIX v4, Table 1 -----------------------------------------------------------
print("FELIX v4 organism (Table 1)")
v4 = load("felix-v4_generational_fitness.csv")
check_eq("runs", len(v4), 5)
g0, g1_, g2 = (col(v4, k) for k in ("gen0_fitness", "gen1_fitness", "gen2_fitness"))
check_eq("runs with Gen0 < Gen1 < Gen2", sum(a < b < c for a, b, c in zip(g0, g1_, g2)), 5)
for label, xs, want in [("mean Gen 0", g0, 0.5471), ("mean Gen 1", g1_, 0.8303),
                        ("mean Gen 2", g2, 1.2477)]:
    check(label, mean(xs), want, 0.00011)
def check_ratio(label, num, den, reported_pct):
    """Fitness is printed to 4 decimals, the gain to 1, so the paper's gain was
    computed from unrounded fitness. Pass if the gain range allowed by the
    fitness rounding overlaps the reported value's rounding range."""
    global failures
    h = 0.00005
    lo = 100 * ((num - h) / (den + h) - 1)
    hi = 100 * ((num + h) / (den - h) - 1)
    ok = lo <= reported_pct + 0.05 and hi >= reported_pct - 0.05
    failures += not ok
    print(f"  {'ok  ' if ok else 'FAIL'} {label}: recomputed {lo:.2f} to {hi:.2f}, reported {reported_pct:g}")


for row in v4:
    a, b, c = (float(row[k]) for k in ("gen0_fitness", "gen1_fitness", "gen2_fitness"))
    check_ratio(f"{row['run']} gain G0->G1 (%)", b, a, float(row["delta_g0_g1_pct"]))
    check_ratio(f"{row['run']} gain G0->G2 (%)", c, a, float(row["delta_g0_g2_pct"]))
check("mean delta G0->G2 (%)", mean(col(v4, "delta_g0_g2_pct")), 129.7, 0.051)

print()
if failures:
    print(f"{failures} check(s) failed")
    sys.exit(1)
print("All checks passed.")
