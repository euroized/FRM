# Preregistration: follow-up tests of FRM (FELIX-C3)

**Status: draft, not yet registered. No mission in this plan has been run.**
Register it publicly before any code for these studies is written. The OSF
registry gives an independent timestamp, and the Registered Reports format at
a journal gets the design peer-reviewed before results exist. Record the commit
hash of this file in the registration.

Three studies follow from what the Stage 3 paper (FELIX-C3 v1.3) leaves open:

| Study | Question | Why it matters |
|---|---|---|
| **T1** | Does FRM's improvement loop beat simple search methods given the same budget? | All three Stage 3 conditions share the loop, so its +12 pp gain has no outside reference. |
| **T2** | What is the most any fixed Imp could be worth? | If even the best fixed Imp is worth less than +1 pp, rewriting Imp cannot clear the bar in this domain. |
| **T3** | Does rewriting Imp help over long, non-stationary missions, with enough power to detect +1 pp? | Stage 3 tested 32 rounds in a fixed domain with about 50% power at +1 pp. |

Run order: T2 first, because it decides whether T3 should run in the
stationary domain; T1 independently; then T3.

## Shared rules

Everything not listed here is carried over unchanged from FELIX-C3 v1.3:

- the task domain and audit gate (§5.5, §6)
- the supervisor and fault suite (§8)
- the statistics (§7.5)

**Freeze.** Each study gets its own freeze record before its Gate 0. The
record holds the source hashes, the configuration, the initial Imp and this
file's commit hash. It is posted with a server timestamp. After the freeze
there are no source, rule, seed or threshold changes and no reruns.

**Seeds.** All ranges below must be checked against the author's records as
never used by any earlier stage or development run before registration. If a
range was used, replace it before registering, not after.

| Use | Seeds |
|---|---|
| T1 pilot | 8501–8508 |
| T1 confirmatory | 8601–8624 |
| T2 search panel (development families only) | 1501–1508 |
| T2 confirmation | 8701–8724 |
| T3 pilot | 8801–8808 |
| T3 confirmatory | 8901–8948 |

**Decision rule.** Every confirmatory contrast is a paired, one-sided exact
Wilcoxon signed-rank test on per-seed differences in test solve rate, as in
C3 Appendix C. A contrast passes only if both hold:

1. p < α, where α is given per contrast;
2. the observed mean difference is ≥ **+0.5 pp**.

This deliberately changes the Stage 3 rule, which required the observed mean
to be ≥ +1.0 pp. When the true effect equals the +1.0 pp bar, that rule fails
about half the time regardless of sample size, which caps its power near 57%.
`protocols/power.py` shows this on the Stage 3 data. Under the rule above, the
study is powered for a true +1.0 pp effect, and the +0.5 pp floor stops a
significant but trivial difference from passing.

**Reporting.** Every outcome is reported, whatever it is: PASS, FAIL, NO-GO or
an invalid study. Results are evaluated only by `protocols/analyze.py` at the
commit named in the registration.

## T1: outside baselines at the same budget

**Arms.** All arms run 32 rounds on the same task streams. Each round has the
same 8 candidates, the same selection batch, the same external audit and the
same evaluation budget.

- **LOOP**: FRM with Imp frozen at its initial value, which is condition C6f.
  It is the loop without recursion, and in Stage 3 it matched C6 (B-1 null).
- **RS**: the proposer is replaced by uniform random sampling from the same
  revision space. It has the same vocabulary and the same distribution of
  revision sizes, and it reads no evidence.
- **ES**: a (1+8) evolution strategy. Each candidate is the incumbent policy
  plus independent Gaussian perturbations of its parameters. σ is fixed in the
  freeze record from development seeds only.

Screening, audit, integration and test measurement are identical across arms.
The freeze record must define RS and ES exactly, because the policy
representation is withheld from the papers.

**Gates.**
- Gate 0 checks determinism, as in Stage 3.
- Gate 1 is a pilot on 8501–8508. It returns GO if the bootstrap power for
  T1-P at n = 24 is ≥ 0.5; otherwise the result is NO-GO and is reported.

**Contrasts** (round 32, confirmatory seeds 8601–8624):

| ID | Contrast | α | Role |
|---|---|---|---|
| T1-P | LOOP − RS | 0.01 | primary |
| T1-S | LOOP − ES | 0.01 | secondary |

**Interpretation.**
- A PASS on T1-P shows that the loop's evidence use beats undirected search.
- A FAIL means the +12 pp gain comes from the audited hill-climb, not from
  diagnosis.

**Approximate cost:** 96 missions, about 10 machine-hours.

## T2: the best a fixed Imp can do

**Search.** 64 Imp configurations are drawn uniformly within each parameter's
registered bounds, using a seed fixed in the freeze record. Together with the
default, each configuration runs one 32-round mission on each of panel seeds
1501–1508, on development families only. The configuration with the highest
mean test solve rate is **BEST**. Any tie is broken by the lower configuration
index.

**Confirmation.** BEST and DEFAULT each run on fresh seeds 8701–8724. BEST is
chosen on the panel and judged only on fresh seeds, so the estimate carries no
selection bias.

**Estimate** (not a pass/fail test). T2-P is BEST − DEFAULT at round 32, given
as a mean with a 95% bootstrap interval:

- **BOUNDED** if the upper limit of the interval is < +1.0 pp. No fixed Imp is
  worth +1 pp in this domain, so rewriting Imp cannot clear the bar here, and
  T3 runs only in its non-stationary form.
- **HEADROOM** otherwise.

**Approximate cost:** 520 search missions plus 48 confirmation missions, about
60 machine-hours.

## T3: long-horizon, non-stationary, powered test of recursion

**Arms.** The three Stage 3 conditions, unchanged:

- **C6**: Imp rewritable, adopted on evidence
- **C6f**: Imp frozen
- **C6r**: Imp rewritten, with adoption by coin flip

**Missions.** Each mission runs 128 rounds, with test checkpoints at 0, 32, 64,
96 and 128.

**Non-stationarity.** At rounds 32, 64 and 96 the training stream switches to a
different 6-of-12 subset of the development families. The schedule is derived
from the freeze hash. The 4 held-out families stay held out. The test set
covers all 16 families throughout.

This is the setting in which an adaptive improvement mechanism has the most
room to beat a fixed one. The FELIX v4 work also found that a stationary
environment exhausts the search.

**Sample size.** 48 confirmatory seeds (8901–8948). From `power.py` (B-1 noise
model, SD 2.06 pp), power under the decision rule above is:

| True effect | Power |
|---|---|
| +1.0 pp | 0.87 |
| +1.5 pp | 0.99 |

This assumes that the variance at round 128 is close to the variance at round
32. The pilot re-estimates it.

**Gates.**
- Gate 0 checks determinism and headroom, as in Stage 3.
- The pilot runs on 8801–8808. Its pilot variance is reported. If it implies
  power < 0.8 at +1.0 pp with 48 seeds, the seed count is raised **before**
  the confirmatory freeze, by the rule n = ⌈48 × (s_pilot / 2.06)²⌉.

**Contrasts** (round 128):

| ID | Contrast | α | Role |
|---|---|---|---|
| T3-P | C6 − C6f | 0.01 | primary |
| T3-S | C6 − C6r | 0.05 | secondary |

The contrasts at rounds 32, 64 and 96 are reported descriptively.

**Approximate cost:** 144 confirmatory missions of 128 rounds, plus the pilot,
about 70 machine-hours. This assumes mission time grows linearly with rounds;
Stage 3 averaged about 6.4 minutes per 32-round mission.

## Results file

`analyze.py` reads one CSV with the columns

```
study, seed, arm, round, test_solve_pct
```

Arms are `LOOP`, `RS`, `ES` (T1); `BEST`, `DEFAULT` (T2); `C6`, `C6F`, `C6R`
(T3). A template is in [`results_template.csv`](results_template.csv). The
script refuses to evaluate a study whose seeds fall outside the registered
range or that has any seed/arm pair missing.

`python3 protocols/analyze.py --selftest` checks the pipeline on synthetic
data with known effects. Its numbers are not results.
