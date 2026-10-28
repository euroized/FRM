# FRM-12: preregistration

Written 2026-10-27, after FRM-11's result was known and before any FRM-12 confirmatory mission has run. Its SHA-256 is recorded in `FREEZE12.json` with the hashes of `runner12.py`, `campaign10.py`, the FRM-11 inputs in `frm12/inputs/`, FELIX-C9's freeze hash and FRM-11's freeze hash.

## Why this study exists

FRM-11 (run 40441244896, verdict **"B-1 pass but Tier A fails"**) failed only A-4: E's second-half progress was +1.08 pp with p = 0.026 (bar p < 0.01). Its records also showed two defects, disclosed here:

1. **FRM-11's arm R equalled the default Imp D in both campaigns.** The random-drift control replayed the campaign's proposal steps, which can reset genes or edit only the mechanism. Campaign 0's two drift steps went to trees and back; campaign 1's single step changed only the mechanism. FRM-11's B-2 (E − R) was therefore effectively E − D, not a test of whether evidence matters.
2. **Cross-hardware floating-point differences.** R and D had byte-identical mission specs, yet 6 of 24 pairs diverged at round 1–2. All six divergent missions ran on the same two Actions shards (7 and 8), consistent with a different CPU type giving float-level differences in scikit-learn's solvers. Missions are deterministic on one machine.

FRM-11 stands as reported. FRM-12 is a new study. Any FRM-12 claim comes from FRM-12's data only.

## What was learned before this document (disclosed)

FRM-11's records showed E (trees) saturating by round 16: in its second half, 239 of 384 rounds failed the promotion audit, nearly all with gains under 2% that the 300-task audit could not confirm. Two development pilots on FRM-11's spent confirmatory seeds 9201–9204 (arms E and D, full missions; code, per-mission records and summary in `frm12/pilots/`) compared four settings:

| Setting | A-4 (E r32 − r16) | E − D |
|---|---|---|
| FRM-11 (8 candidates, 96 selection, 300 audit) | −0.16 pp | +4.38 pp |
| 600-task audit, gain_min 0.01 | +0.08 pp | +4.22 pp |
| 900-task audit, gain_min 0.01 | −0.94 pp | +2.34 pp |
| 16 candidates per round | +0.86 pp | +5.08 pp |
| **16 candidates, 192 selection tasks** | **+2.27 pp** | **+6.41 pp** |

The last setting was chosen. Four seeds cannot show significance; the pilots are exploratory and carry no claim.

## Design

**Confirm-only.** FRM-12 runs no new campaigns. Arm E uses the Imps FRM-11's campaigns obtained by themselves (both: learner trees, alloc 1). FRM-11's campaigns ran with the original mission setting; FRM-12 tests their product under the new one. This is stated in every claim.

| Element | Setting |
|---|---|
| Missions | FELIX-C9 frozen code, 32 rounds, forking off (C7f), **candidates_per_round 16, selection_tasks 192**; everything else at FELIX-C9's defaults (task budget 12, audit 300 tasks, gain_min 0.02, audit_p_max 0.10). Training on the 12 development families, testing on all 16 |
| Seeds | **9301–9324**, never used before; seed index i is assigned FRM-11 campaign c = i mod 2 |
| Arm E | Final Imp of FRM-11 campaign c |
| Arm D | FELIX-C9's default Imp |
| Arm R | Evidence-free control, drawn independently per seed: one proposal picked uniformly at random (stream `frm12-R`, c, seed) from all proposals FRM-11 campaign c made; its recorded active part is the arm's Imp. Campaign 0 proposed 32 (9 trees), campaign 1 proposed 54 (7 trees) |
| R's composition | Computed from the fixed stream after the code was written and before the freeze, and not changed: 14 logistic, 3 l1, 3 balanced, 2 pairwise, 2 trees (24 seeds) |
| Execution | One machine (this cloud container), 4 missions at a time, single-threaded numerical libraries (`OMP_NUM_THREADS=1`, `OPENBLAS_NUM_THREADS=1`, `MKL_NUM_THREADS=1`) |

## Criteria (FELIX-C9's, unchanged; exact one-sided Wilcoxon on 24 per-seed differences in round-32 test solve rate)

| ID | Criterion |
|---|---|
| **B-1** | E − D mean ≥ +1.0 pp and p < 0.01 |
| **B-2** | E − R mean ≥ +0.5 pp and p < 0.05 |
| A-1 | Promotions in ≥ 20 of 24 E missions |
| A-2 | Inherited from FRM-11: each campaign committed ≥ 1 edit and its final Imp differs from the default (Gate 1 GO) |
| A-3 | Inherited from FRM-11: the editing procedure is inside the genome and edited by itself |
| **A-4** | E second-half progress (round 32 − round 16): mean ≥ +1.0 pp and p < 0.01 |
| A-5 | Sources and inputs match the freeze; all 72 missions reconcile |
| Headroom, autonomy | D mean ≤ 0.85; 0 interventions |

**Verdict:** "Productive recursion: Level 4 with causal support" requires Tier A (A-1 to A-5), B-1 and B-2.

**Further claims (gated on that verdict, as in the FRM-11 addenda):**
- **Self-obtained:** SO-1 in each campaign's 12 seeds (E − D mean > 0, p < 0.05).
- **Transfers to held-out families:** H-1 (E − D held-out ≥ +1.0 pp, p < 0.005) and H-2 (E − R held-out ≥ +0.5 pp, p < 0.025).

Not in FRM-12: the generation-2 "sustained" test and the real-bug test; both need their own runs.

## What a pass would and would not show

A pass shows that the Imp FRM-11's system obtained by itself, under a wider search, meets every rung of FELIX's Level-4 ladder with causal support on fresh seeds. It does not show that campaigns run under the new setting would obtain the same Imp (they were not run), and it says nothing about held-out families or real bugs unless H-1/H-2 pass.

## Not allowed after the freeze

Any change to code, inputs, settings, seeds or criteria. A crash is resumed crash-only from checkpoints and logged; no mission is dropped or rerun selectively.

Design and implementation were done with AI assistance (Claude).
