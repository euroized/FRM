# FRM-11: preregistration

Written 2026-10-27, before any full-scale FRM-11 mission has run. Its SHA-256 is recorded in `FREEZE11.json`, together with the hashes of `runner11.py` and `campaign10.py` and FELIX-C9's freeze hash. Changing any of them changes the freeze hash.

## Question

Does FELIX-C9, with its campaign replaced by the FRM-10 campaign (`campaign10.py`), meet FELIX's Level-4 ladder **with causal support**? That is, does the system's own self-editing campaign produce an improvement mechanism (Imp) that beats both the default Imp and evidence-free rewriting, on fresh seeds?

## System under test

- **Missions:** FELIX-C9, frozen and unmodified (freeze hash `42288423f6b26e5eef87e3f02285fab136fd628a2282d0ae285be4ab2643dedd`). Full-scale 32-round missions with in-mission forking off (arm C7f). Training on the 12 development families; testing on all 16.
- **Campaign:** `campaign10.py`, unchanged from FRM-10 (SHA-256 `e43ffbe894c1bdeae71ae91086443a08fa5a49abe96ef75a61e2425afa077038`, as recorded in `FREEZE10.json`). The writable genome is the full Imp, the improver program (which edits itself) and the pool rules. The fixed gate is outside the genome: a candidate becomes the incumbent only if its total on 4 hidden seeds beats the incumbent's by more than 1 task per seed.
- **Campaign settings:** 2 campaigns, seed bases 41000 and 42000. Public panel of 2 seeds, scored on both; hidden seeds at base + 500 to + 503. Noise scale 5 tasks. Each campaign stops at its first step that starts with ≥ 48 unique missions. This budget is the one at which FRM-10's Study 3 campaigns reached the tree learner in 89–97% of runs (disclosed: chosen after seeing that interim result).

## Arms (confirmatory)

24 fresh seeds, 9201–9224, never used before. Seed s is assigned campaign c(s) = index mod 2. Arms differ only in their Imp.

| Arm | Imp |
|---|---|
| **E** | Final Imp of campaign c(s) |
| **D** | FELIX-C9's initial (default) Imp |
| **R** | Evidence-free control: from the initial genome, `campaign10.propose` applied once per commit of campaign c(s), every proposal accepted regardless of evidence, on the fixed random stream `drift11` |

Arm T (designer's tree setting) is not run; in FELIX-C9 it was reported only.

**Stated in advance:** on stream `drift11`, the first drift step for campaign 0 is the tree learner. If campaign 0 commits exactly once, R equals E's likely learner on campaign-0 seeds and B-2 has little room there. This was found during dry tests and is left unchanged.

## Criteria (FELIX-C9's locked criteria, unchanged)

All tests: one-sided exact Wilcoxon signed-rank (FELIX-C9 `stats.py`) on the 24 per-seed paired differences in round-32 test solve rate.

| ID | Criterion |
|---|---|
| **B-1** | Rewriting pays off: E − D mean ≥ +1.0 pp and p < 0.01 |
| **B-2** | Evidence matters: E − R mean ≥ +0.5 pp and p < 0.05 |
| A-1 | Promotions in ≥ 20 of 24 E missions |
| A-2 | Each campaign commits ≥ 1 edit, and its final Imp differs from the default in its active part |
| A-3 | The editing procedure (improver program and pool rules) is inside the genome and edited by the same procedure. Self-edits adopted into the final mechanism, and archived mechanism edits, are reported |
| A-4 | E second-half progress (round 32 − round 16): mean ≥ +1.0 pp and p < 0.01 |
| A-5 | Integrity: sources match the freeze; every campaign and confirmatory mission reconciles (receipt chain, spend, weights, no fork, Imp unchanged); every campaign log replays to the same decisions and final Imp |
| Headroom | D mean ≤ 0.85, otherwise INVALID |
| Autonomy | 0 interventions across all missions |

**Verdict**

| Verdict | Requires |
|---|---|
| **Productive recursion: Level 4 with causal support** | Tier A (A-1 to A-5), B-1 and B-2 |
| Partial | Tier A and B-1 only |
| FAIL on the causal question | B-1 fails |

All verdicts are reported, whatever they are.

## Reported, not criteria

Per-campaign E − D; held-out and development splits of E − D; R − D; each campaign's final learner and mechanism; R's learner; commits and gate checks; mission and evaluation counts.

## Gates

- **Gate 0:** sources match their freezes; a tiny campaign10 campaign (dry missions, development seeds 1450–1463) killed mid-run, with its mission workers, resumes to the same log head, history and final Imp as an uninterrupted run, and both replay.
- **Gate 1 (A-2):** if either campaign commits nothing, or its final Imp equals the default, the study stops and is reported. Otherwise the confirmatory runs once.

## Execution (disclosed)

- **Hardware:** GitHub-hosted Actions runners (Linux, 2 vCPU), on a private repository. Python 3.13, numpy 2.5.3, scikit-learn 1.9.1, pinned.
- **Sharding:** the two campaigns run on separate runners; the 72 confirmatory missions are split into fixed shards (mission k, k + n, …). Sharding and worker counts change speed only; missions are deterministic.
- **Interruptions:** jobs have a time limit. A job that reaches its limit kills its process group and saves its state; the next job resumes crash-only. Every interruption is logged.
- **Known non-determinism (as disclosed in FELIX-C9 v1.2 §11):** the decoy learner `l1` calls scikit-learn's `liblinear` solver without a seed, so a mission whose Imp uses `l1` is not bit-reproducible, and a campaign that proposes `l1` can follow a different path on a rerun. Dry tests here confirmed that every divergence between reruns came from `l1` missions; all other learners reproduced exactly. FELIX-C9's frozen code is not changed to fix this. Every decision is recorded and replays exactly from the stored mission records (A-5). Gate 0's crash-test seed proposes no `l1` candidate.
- **Before this document:** only dry smoke tests (tiny missions, development seeds 1450–1499) and a scripted-evaluator test of the commit path. No full-scale FRM-11 mission had run.
- **Not allowed after the freeze:** any change to code, settings, seeds or criteria. A defect that stops the run is fixed only by a new freeze, disclosed with the reason, before any confirmatory mission runs.

Design and implementation were done with AI assistance (Claude).
