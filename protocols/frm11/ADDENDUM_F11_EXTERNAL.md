# FRM-11 addendum: external criteria

Written 2026-10-27, while the FRM-11 campaigns were running (run 40441244896, started 02:55 UTC) and **before any campaign result, Gate 1 record, confirmatory mission or real-bug unit existed**. It adds criteria; it changes nothing in `PREREGISTRATION_F11.md`, `FREEZE11.json` or any code that run uses. Its SHA-256 is fixed by the commit that adds it, and `ext_analysis.py` (same commit) is the only code that applies it.

## Why

FRM-11's ladder is scored on FELIX's synthetic repair tasks, on all 16 families. Passing it shows Level 4 with causal support **in that domain**. It does not show that the rewriting helps outside the families the campaigns trained on, or on real bugs. In FELIX-C9 it did neither: held-out E − D +0.26 pp (n.s.), real-bug E − D +0.39 bugs (p = 0.52). This addendum makes both explicit pass/fail criteria, fixed before the data.

## Criteria

All per-seed paired differences over the 24 confirmatory seeds 9201–9224, campaign c(s) = index mod 2. Exact one-sided Wilcoxon signed-rank (FELIX-C9 `stats.py`, zeros dropped).

**Held-out families (H).** Score: mean round-32 solve rate over the 4 held-out families (`held_out_families` in `FREEZE11.json`, as derived for FELIX-C9), from each confirmatory mission's `result.by_family`.

| ID | Criterion |
|---|---|
| **H-1** | E − D mean ≥ +1.0 pp and p < 0.005 |
| **H-2** | E − R mean ≥ +0.5 pp and p < 0.025 |

**Real bugs (X).** Score: bugs solved out of FELIX-C7's 164 (QuixBugs-Python and HumanEvalFix-Python), mean over its S = 8 tie-break seeds, budget 12, exactly as `frozen/realbugs9.py` computes it. The policy is each confirmatory mission's round-32 policy. Requires the frozen FELIX-C7 pipeline at freeze `0b9617b8d2fd774dda7a6fec001fbb9d429888617ceb3730a4874a7fea37aec0`.

| ID | Criterion |
|---|---|
| **X-0** | Transfer replicates: E − r0 mean > 0 and p < 0.01 (r0 = the empty starting policy) |
| **X-1** | E − D mean ≥ +1.0 bug and p < 0.005 |
| **X-2** | E − R mean ≥ +0.5 bug and p < 0.025 |

## Claims and order

Testing is gated: nothing below is claimed unless the step above it passed.

| Claim | Requires |
|---|---|
| **L4 (in-distribution)** | The FRM-11 verdict "Productive recursion: Level 4 with causal support" |
| **L4 transfers to held-out families** | L4 in-distribution, then H-1 and H-2 |
| **L4 on real bugs (external)** | L4 in-distribution, then X-0, X-1 and X-2 |

The held-out and real-bug claims are tested in parallel after the gate, each at half the ladder's α (p < 0.005 and p < 0.025 in place of 0.01 and 0.05), so that together they keep the ladder's error rate. All results are reported, pass or fail.

## Reproduction (R)

A result is called **independently reproduced** only if a party other than the author reruns this repository's frozen commit on their own hardware and obtains:
- the same two campaign final Imp hashes, and
- per-seed round-32 solve rates identical to the original for every confirmatory mission whose Imp does not use the `l1` learner (`l1` is not bit-reproducible; see the preregistration), and
- the same verdict for every claim above.

## Run

```
python3 ext_analysis.py heldout            # after evaluate: H-1, H-2 from the confirmatory records
python3 ext_analysis.py realbugs C7_DIR    # after realbugs: X-0, X-1, X-2 (needs the FELIX-C7 pipeline)
python3 ext_analysis.py claims             # the gated claims, from confirm_results.json and the two outputs above
```
