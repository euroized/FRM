# FRM-11 addendum 2: self-obtained and sustained

Written 2026-10-27, while the FRM-11 campaigns (run 40441244896) were still running and **before any campaign result, Gate 1 record or confirmatory mission existed**. It adds criteria and one follow-up run; it changes nothing in `PREREGISTRATION_F11.md`, `FREEZE11.json`, `ADDENDUM_F11_EXTERNAL.md` or any code those use. `ADDENDUM_HASHES.txt` (same commit) fixes the hashes of this file and of the code that applies it (`sustain.py`, `.github/workflows/sustain.yml`, `ext_analysis.py`); every job of the follow-up checks them.

## Why

FRM-11's verdict "Level 4 with causal support" pools both campaigns. In FELIX-C9 the pooled result rested on one campaign (campaign 0 +5.70 pp; campaign 1 −0.57 pp), and nothing tested whether the gain lasts once the system keeps modifying itself. This addendum makes both explicit.

## Self-obtained (SO)

The gain must be obtained by the system itself, in **each** independent campaign:

| ID | Criterion |
|---|---|
| A-2, autonomy, B-2 | As preregistered: each campaign commits through its fixed gate on its own hidden-seed evidence; 0 interventions; E beats evidence-free rewriting |
| **SO-1** | In **each** campaign separately, on its own 12 confirmatory seeds: E − D mean > 0 and one-sided Wilcoxon p < 0.05 |

## Sustained (SU): generation 2

Each campaign runs a **second generation**: it starts from generation 1's committed genome (final Imp, and the final improver program and pool rules, including any self-edits), runs the same `campaign10` loop with the same budget (48 unique missions) and the same fixed gate, on fresh seeds (bases 43000 and 44000, hidden at + 500), on its own random stream (c + 10). Its final Imp is arm **E2**, run on the same 24 confirmatory seeds (9201–9224) as E, D and R.

| ID | Criterion (24 per-seed paired differences, exact one-sided Wilcoxon) |
|---|---|
| **SU-1** | The gain persists: E2 − D mean ≥ +1.0 pp and p < 0.01 |
| **SU-2** | No regression: E2 is non-inferior to E with margin 0.5 pp (test on E2 − E + 0.5 pp: mean > 0 and p < 0.05) |
| **SU-3** | Still evidence-driven: E2 − R mean ≥ +0.5 pp and p < 0.05 |
| Integrity | Generation-2 logs replay; all 24 E2 missions reconcile; sources and addendum hashes match |

**Reported, not criteria:** E2 − E (does the gain accumulate?), generation-2 commits, whether the mechanism self-edited again, E2 − D on held-out families.

If generation 2 commits nothing, E2 equals E and SU-2 passes trivially; SU-1 then repeats B-1 on the same missions. This is reported as "sustained without further gain", not as accumulation.

## Claims

| Claim | Requires |
|---|---|
| **L4 (in-distribution)** | FRM-11 verdict "Productive recursion: Level 4 with causal support" |
| **L4, self-obtained** | L4 and SO-1 in both campaigns |
| **L4, self-obtained and sustained** | L4, self-obtained, SU-1, SU-2, SU-3 and integrity |

Each claim adds conditions to the one above (an intersection test), so no further α adjustment is needed. The held-out and real-bug claims of `ADDENDUM_F11_EXTERNAL.md` are unchanged.

## Run

GitHub Actions → **FRM-11 sustain**, with `from_run` = the completed FRM-11 run's ID, after its Gate 1 is GO. Locally:

```
python3 sustain.py campaign 0 & python3 sustain.py campaign 1 & wait
python3 sustain.py confirm
python3 sustain.py evaluate
```

Cost: about 3–5 h wall clock (two campaigns in parallel, then 24 missions on 4 runners), about 600–800 runner minutes.
