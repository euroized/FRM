# FRM-11 and FRM-12: results

Two preregistered tests of whether FRM meets FELIX's Level-4 ladder with causal support when FELIX-C9's campaign layer is replaced by the FRM-10 campaign: an archive of variants, an improver program that edits itself, writable parent-selection rules, and a fixed adoption gate outside the genome. FELIX-C9's frozen mission code (freeze `42288423…2643dedd`) was used unchanged in both.

**Verdict of both studies: "B-1 pass but Tier A fails."** The rewrite the system obtained by itself caused a large, replicated gain (B-1), and FRM-12 showed it was evidence-driven rather than random (B-2). Both studies failed A-4 (sustained progress within the mission). Neither study supports the claim "Level 4 with causal support."

## Registration and timing

The protocols were registered in a private repository before any of their data existed. They are published here after the results, byte-identical to the registered files: their SHA-256 values are in the freeze records and in `frm11/ADDENDUM_HASHES.txt`.

| Document | Registered (private repository, UTC) | First data |
|---|---|---|
| `frm11/PREREGISTRATION_F11.md`, `frm11/FREEZE11.json` (freeze `6d735312…`) | 2026-10-27 02:46 | Campaigns started 02:58 |
| `frm11/ADDENDUM_F11_EXTERNAL.md` (held-out and real-bug criteria) | 04:11 | Campaign results 06:22 |
| `frm11/ADDENDUM_F11_SUSTAINED.md` (self-obtained and sustained criteria) | 04:28 | Campaign results 06:22 |
| `frm12/PREREGISTRATION_F12.md`, `frm12/FREEZE12.json` (freeze `2aa99acc…`) | 21:30, after FRM-11's result | Missions started 21:31 |

These timestamps are commit times in the private repository. They are not a public registry.

## FRM-11

**Design.** Two campaign10 campaigns (seed bases 41000 and 42000, 48 unique full-scale missions each), then 24 fresh confirmatory seeds (9201–9224) × 3 arms: E (the campaign's final Imp), D (default Imp) and R (an evidence-free control). It ran on GitHub-hosted Actions runners.

**Campaigns.** Both independently committed the tree learner, through the fixed gate, on their own hidden-seed evidence: campaign 0 made 2 commits, campaign 1 made 1. Campaign 1's final mechanism had self-edited.

| | Criterion | Result |
|---|---|---|
| ✅ | A-1 promotions in ≥ 20/24 E missions | 24/24 |
| ✅ | A-2 each campaign commits; E ≠ default | 2, 1; both trees |
| ✅ | A-3 editing procedure inside the genome | yes |
| ❌ | **A-4** E round 32 − round 16 ≥ +1.0 pp, p < 0.01 | **+1.08 pp, p = 0.026** (15/5/4) |
| ✅ | A-5 integrity | 72/72 missions reconciled; campaign logs replay |
| ✅ | Headroom, autonomy | D = 40.6%; 0 interventions |
| ✅ | **B-1** E − D ≥ +1.0 pp, p < 0.01 | **+4.71 pp, p = 1.2 × 10⁻⁷** (23/1/0) |
| ✅* | B-2 E − R ≥ +0.5 pp, p < 0.05 | +5.00 pp, p = 6 × 10⁻⁸ (24/0/0); *see defect 1* |

Reported: each campaign's E − D was +4.35 pp (11/1) and +5.08 pp (12/0). On held-out families E − D was −1.67 pp (p = 0.96), and on development families +6.84 pp. Because the L4 verdict was not reached, the gated claims of the addenda (held-out, real bugs, self-obtained, sustained) were not claimed. The generation-2 "sustained" run and the real-bug test were not run.

**Defects found in FRM-11's records after the run (disclosed in FRM-12's preregistration):**
1. **Arm R equalled the default Imp D in both campaigns.** The random-drift control replayed the campaign's own proposal steps, and these can reset genes or edit only the mechanism. Campaign 0's two drift steps went to trees and back; campaign 1's single step changed only the mechanism. FRM-11's B-2 was therefore effectively a second E − D, not a test of whether evidence matters.
2. **Cross-hardware floating-point differences.** R and D had byte-identical mission specs, yet 6 of 24 pairs diverged after round 1–2. All six divergent missions ran on the same two runner shards, which is consistent with a different CPU type producing float-level differences in scikit-learn's solvers. Missions are deterministic on one machine.

## Between the studies (exploratory, disclosed)

FRM-11's records showed E (trees) saturating by round 16. Two development pilots on FRM-11's spent seeds 9201–9204 compared settings (`frm12/PILOT_SUMMARY.txt`):

| Setting | A-4 (E r32 − r16) | E − D |
|---|---|---|
| FRM-11's setting | −0.16 pp | +4.38 pp |
| 600 / 900 audit tasks, gain_min 0.01 | +0.08 / −0.94 pp | +4.22 / +2.34 pp |
| 16 candidates per round | +0.86 pp | +5.08 pp |
| 16 candidates, 192 selection tasks | +2.27 pp | +6.41 pp |

The last setting was chosen for FRM-12. Its A-4 gain did not replicate on 24 seeds (below), so a four-seed pilot was too small to choose a setting from.

## FRM-12

**Design.** Confirm-only: no new campaigns. Arm E is the Imp FRM-11's campaigns obtained by themselves (trees). All missions use 16 candidates per round and 192 selection tasks. Arm R is a real evidence-free control: for each seed, one of the campaign's own proposals is picked uniformly at random on a fixed stream (14 logistic, 3 l1, 3 balanced, 2 pairwise, 2 trees). It used 24 fresh seeds (9301–9324) and ran on one cloud machine with single-threaded numerical libraries. The run was interrupted twice by host restarts and resumed crash-only from checkpoints (`results/FRM12_interruptions.jsonl`); no mission was dropped or rerun selectively.

| | Criterion | Result |
|---|---|---|
| ✅ | A-1 promotions | 24/24 |
| ✅ | A-2, A-3 (inherited from FRM-11's campaigns) | as above |
| ❌ | **A-4** E round 32 − round 16 ≥ +1.0 pp, p < 0.01 | **+0.81 pp, p = 0.021** (13/6/5) |
| ✅ | A-5 integrity | 72/72 missions reconciled |
| ✅ | Headroom, autonomy | D = 40.6%; 0 interventions |
| ✅ | **B-1** E − D | **+4.92 pp, p = 6 × 10⁻⁸** (24/0/0) |
| ✅ | **B-2** E − R | **+4.69 pp, p = 2.4 × 10⁻⁷** (22/0/2) |
| — | SO-1 per campaign (gated) | +4.92 pp, 12/0 in each (E is the same Imp in both) |
| ❌ | H-1 / H-2 held-out (gated) | −1.30 pp / −0.73 pp |

The random-proposal control did no better than the default (R − D +0.23 pp, p = 0.29).

## What the two studies show

- **The self-obtained rewrite causes the gain, and the gain replicates:** E − D was +4.71 pp (FRM-11) and +4.92 pp (FRM-12) on separate fresh seeds. FELIX-C9's comparable figure was +2.57 pp, resting on one of its two campaigns. Here both campaigns found the structure independently.
- **The choice is evidence-driven** (FRM-12 B-2): picking at random from the same proposals gives no gain over the default.
- **A-4 fails for a structural reason.** E reaches about 44–45% by round 16 and gains under 1 pp after that, in both studies and under every pilot setting: the tree learner converges within half a mission. A-4 was defined in Stage 3 for slower linear learners. It is not redefined here after the fact.
- **No transfer to held-out families**, as in every earlier study.

## Files

| Path | What it is |
|---|---|
| `frm11/` | FRM-11 preregistration, both addenda, their hashes, freeze record |
| `frm12/` | FRM-12 preregistration, freeze record, pilot summary |
| `results/FRM11_results.json`, `results/FRM12_results.json` | Full evaluation output, per seed |
| `results/FRM11_ladder.txt`, `results/FRM12_ladder.txt` | The printed ladders |
| `results/FRM11_gate1.json`, `results/FRM12_interruptions.jsonl` | Gate 1 record; FRM-12's restart log |
| `../data/frm11_per_seed.csv`, `../data/frm12_per_seed.csv` | Per-seed round-16 and round-32 solve rates, held-out rates and promotions for E, D and R; `data/verify.py` recomputes the numbers above from them |

Mission records, campaign logs and the source code are held privately and available to reviewers on request, as for the earlier studies.
