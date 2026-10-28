# Follow-up tests T1–T3: status

These are independent follow-up tests of the frozen Stage 3 system (FELIX-C3).
They were designed after the Stage 3 paper and registered in this public
repository. [`PREREGISTRATION.md`](PREREGISTRATION.md) is kept exactly as it
was registered at commit `4908d9b`; each study's freeze record in
[`freeze/`](freeze/) points to that commit. The header of that file still says
"draft"; this page gives the current status.

| Study | Question | Status | Result |
|---|---|---|---|
| **T1** | Does the improvement loop beat simple search at the same budget? | **Complete** (confirmatory, seeds 8601–8624) | **PASS.** Loop − random search +11.37 pp [10.20, 12.50], 24/24 seeds, p = 6 × 10⁻⁸; loop − (1+8) evolution strategy +12.20 pp, 24/24, p = 6 × 10⁻⁸ |
| **T2** | What is the most any fixed Imp could be worth? | **Paused.** The configuration search finished; the confirmation was stopped at 33 of 48 missions to free compute, and can resume from checkpoints | No estimate is reported until the confirmation completes |
| **T3** | Does rewriting Imp help over long, non-stationary missions? | **Not run** (the pilot is frozen, not started) | — |

**FRM-11 and FRM-12** are later preregistered tests of FELIX-C9 with the FRM-10 campaign layer, against FELIX's Level-4 ladder. Both are complete, and both have the verdict **"B-1 pass but Tier A fails"**. The self-obtained rewrite beat the default Imp by +4.71 pp (FRM-11, 23/24 seeds) and +4.92 pp (FRM-12, 24/24), and in FRM-12 beat a random pick from the system's own proposals by +4.69 pp (22/0/2). Both failed A-4, sustained within-mission progress (+1.08 pp, p = 0.026; +0.81 pp, p = 0.021; the bar is p < 0.01). Neither showed a held-out gain. Full results, defects found and timings: [`FRM11_FRM12_RESULTS.md`](FRM11_FRM12_RESULTS.md).

## T1 in brief

The loop is Stage 3 condition C6f: the improvement loop with Imp frozen. The
baselines replace only its proposer, with evidence-free random search (RS) or
a (1+8) evolution strategy (ES). Everything else is shared: screening, the
external audit on 300 fresh tasks, 12 evaluations per task, and 32 rounds.

| Arm | Round 0 | Round 16 | Round 32 | Held-out families, round 32 | Evaluations per mission |
|---|---|---|---|---|---|
| Loop | 27.32% | 37.77% | **39.60%** | 31.04% | 362k |
| RS | 27.32% | 27.49% | 28.23% | 25.89% | 428k |
| ES | 27.32% | 27.42% | 27.40% | 25.89% | 384k |

The baselines spent more evaluations than the loop, so the comparison does not
favour the loop on budget. The loop's round-32 mean on these fresh seeds
(39.60%) is close to the Stage 3 C6f mean (39.8%).

T1 shows that the improvement loop's gain is not something any search over
policies would produce at this budget. It says nothing about rewriting Imp,
which T1 does not test.

## Files

| Path | What it is |
|---|---|
| [`PREREGISTRATION.md`](PREREGISTRATION.md) | The registered protocol for T1–T3 |
| [`freeze/`](freeze/) | Freeze records (T1, T2, T3) and the T1 Gate 1 record, each written before its missions ran |
| [`results/`](results/) | T1 per-seed results, analysis output and summary |
| [`analyze.py`](analyze.py) | Applies the registered decision rules (`--selftest` checks it on synthetic data) |
| [`power.py`](power.py), [`power_results.txt`](power_results.txt) | Power analysis behind the seed counts |
| [`results_template.csv`](results_template.csv) | The results format `analyze.py` reads |
| [`OSF_REGISTRATION_TEMPLATE.md`](OSF_REGISTRATION_TEMPLATE.md) | Template and steps for registering future studies on OSF |
| [`FRM11_FRM12_RESULTS.md`](FRM11_FRM12_RESULTS.md) | FRM-11 and FRM-12: results, disclosed defects, registration timings |
| [`frm11/`](frm11/), [`frm12/`](frm12/) | Their preregistrations, addenda, hashes and freeze records, byte-identical to the registered files |
| `results/FRM11_*`, `results/FRM12_*` | Their evaluation output, ladders, Gate 1 record and restart log |

## Deviations and disclosures

- T1 and T2 deviations from the draft are listed in their freeze records.
- The runs used a different machine and library versions from Stage 3. Before
  freezing T1, four Stage 3 confirmatory missions were rerun and matched the
  published per-seed values exactly, and the harness was shown to reproduce a
  frozen Stage 3 receipt chain byte for byte.
- The container running the studies was restarted several times. Every
  restart was logged, all missions resumed from their checkpoints, and no seed
  was dropped.
- The source code is not in this repository. The freeze records list source
  file hashes only.
