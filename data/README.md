# Data

These are machine-readable copies of the per-seed result tables printed in the
papers. Each CSV reproduces one table exactly as printed, including its
rounding. Nothing here comes from the confidential audit packages.

| File | Source | Rows |
|---|---|---|
| [`felix-c3_per_seed_test_solve.csv`](felix-c3_per_seed_test_solve.csv) | FELIX-C3 v1.3, Appendix A, Table 24 (p. 44) | 24 confirmatory seeds (7101–7124) |
| [`felix-c3_gate1_pilot.csv`](felix-c3_gate1_pilot.csv) | FELIX-C3 v1.3, §9.3, Table 10 (p. 18) | 8 pilot seeds (3201–3208) |
| [`felix-c7_per_seed_bugs_solved.csv`](felix-c7_per_seed_bugs_solved.csv) | FELIX-C7 v1.1, Appendix A, Table 7 (p. 22) | 24 seeds (7101–7124) |
| [`felix-c9_per_seed.csv`](felix-c9_per_seed.csv) | FELIX-C9 v1.2, Appendix A, Table 11 (p. 24) | 24 confirmatory seeds (7901–7924) |
| [`felix-v4_generational_fitness.csv`](felix-v4_generational_fitness.csv) | FELIX v4, §5.1, Table 1 (p. 7) | 5 runs |
| [`frm11_per_seed.csv`](frm11_per_seed.csv) | FRM-11 mission records ([`protocols/FRM11_FRM12_RESULTS.md`](../protocols/FRM11_FRM12_RESULTS.md)) | 24 confirmatory seeds (9201–9224) |
| [`frm12_per_seed.csv`](frm12_per_seed.csv) | FRM-12 mission records (same) | 24 confirmatory seeds (9301–9324) |

## Columns

**`frm11_per_seed.csv`, `frm12_per_seed.csv`**: unlike the tables above, these come straight from the mission records, as fractions to 6 decimals (exact: 320 test tasks, 80 held-out). For each arm (E evolved Imp, D default Imp, R evidence-free control): `*_r16` and `*_r32` are the test solve rate at rounds 16 and 32; `*_heldout_r32` is the round-32 rate on the 4 held-out families; `*_accepted` is the number of promotions. `campaign` = seed index mod 2.

**`felix-c3_per_seed_test_solve.csv`**: test solve rate in percent on the
seed's 320 test tasks, printed to 0.1. The conditions are C6 (Imp
rewritable), C6f (Imp frozen) and C6r (rewrites adopted by coin flip).

| Column | Meaning |
|---|---|
| `seed` | Confirmatory seed |
| `r0_pct` | Round 0 (identical across conditions) |
| `c6_r16_pct`, `c6_r32_pct` | C6 at rounds 16 and 32 |
| `c6f_r16_pct`, `c6f_r32_pct` | C6f at rounds 16 and 32 |
| `c6r_r16_pct`, `c6r_r32_pct` | C6r at rounds 16 and 32 |
| `c6_imp_trials` | Imp trials in the C6 mission |
| `c6_imp_adopted` | Adopted Imp edits in the C6 mission |
| `c6_imp_adopted_meta` | Adopted edits that changed the editing procedure |

**`felix-c3_gate1_pilot.csv`**: test solve rate as a fraction, printed to
0.001, on the 12 development families only. The columns are C6 at rounds 0,
16 and 32, then C6f and C6r at round 32.

**`felix-c9_per_seed.csv`**: round-32 test solve rate in percent on the
seed's 320 test tasks, and real bugs solved out of 164 (mean over 8 tie-break
streams), both printed to 0.01. Seeds are assigned to campaign
`seed index mod 2`.

| Column | Meaning |
|---|---|
| `seed`, `campaign` | Confirmatory seed, and the campaign whose final Imp arm E carries |
| `e_r32_pct` | E: the campaign's evolved Imp |
| `d_r32_pct` | D: the default Imp |
| `r_r32_pct` | R: evidence-free replay of the campaign (same number of adopted edits, random generations) |
| `t_r32_pct` | T: the designer's best development setting (reported only) |
| `e_minus_d_pp` | E − D as printed |
| `bugs_e`, `bugs_d`, `bugs_r0` | Real bugs solved by E, D and the empty starting policy r0 |

**`felix-c7_per_seed_bugs_solved.csv`**: real bugs solved out of 164, as the
mean over 8 tie-break streams, printed to 0.01. The budget is 12 evaluations
unless marked `b48`.

| Column | Meaning |
|---|---|
| `r0` | Starting policy (Stage 3 initial state) |
| `c6`, `c6f`, `c6r` | Round-32 end states of each Stage 3 condition |
| `c6_permuted` | C6 with its learned parameters permuted (control) |
| `r0_b48`, `c6_b48` | r0 and C6 at budget 48 |
| `delta_p1` | Primary contrast, `c6 − r0`, as printed |

**`felix-v4_generational_fitness.csv`**: best sustained metabolic-efficiency
fitness per generation, printed to 0.0001. The gains are printed to 0.1%; the
paper computed them before rounding the fitness values.

## Verification

[`verify.py`](verify.py) recomputes the papers' headline statistics from these
files. It uses only the Python standard library. The statistics it recomputes
are:

- every reported mean
- the seed counts
- the Imp-activity totals
- the exact Wilcoxon p-values for C3 criteria A-4, B-1 and B-2, for C7
  contrasts P1, S1, S2, S4 and S5, and for C9 criteria B-1 and B-2, the
  per-campaign split, T − D, E − T, R − D and the S-3 real-bug contrasts
- the v4 generational gains
- for FRM-11 and FRM-12: B-1, B-2, A-4 and held-out E − D (means, seed signs and exact p-values) and each study's verdict, against its own results file in `protocols/results/`

```
python3 data/verify.py
```

Because the tables are rounded, recomputed means can differ from the reported
values in the last printed digit. Recomputed p-values are accepted within a
factor of two. In practice the C7 p-values agree to the printed precision, and
the C3 and C9 ones differ only slightly, for example 0.257 against the
reported 0.23 for C3 B-1, and 0.0033 against 0.0028 for C9 B-1. (Rounding each
C9 rate to its exact value on 320 tasks recovers 0.0028.) CI runs this script on every push and pull request.
