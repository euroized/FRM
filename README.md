# FRM: Felix Runtime Module

[![C3 paper DOI](https://img.shields.io/badge/C3_paper_DOI-10.5281%2Fzenodo.23366534-blue)](https://doi.org/10.5281/zenodo.23366534)
[![Repository DOI](https://img.shields.io/badge/repository_DOI-10.5281%2Fzenodo.23366848-blue)](https://doi.org/10.5281/zenodo.23366848)
[![Papers](https://img.shields.io/badge/papers-5-informational)](papers/)
![Status](https://img.shields.io/badge/status-preprint-lightgrey)
[![Check papers](https://github.com/recurse-root/FRMDevelopment/actions/workflows/check-papers.yml/badge.svg)](https://github.com/recurse-root/FRMDevelopment/actions/workflows/check-papers.yml)
[![License: CC BY 4.0](https://img.shields.io/badge/License-CC_BY_4.0-lightgrey.svg)](LICENSE)

Papers and results for **FRM** (Felix Runtime Module), a bounded
self-improving program-repair system, and the programme of nine
preregistered studies that tested it against a published Level-4 definition
of recursive self-improvement (RSI).

FRM runs inside a fixed boundary that it cannot change. In each round it
proposes revisions of its own repair policy, screens them, and promotes a
revision only if it passes an external audit on fresh tasks. The rule that
turns evidence into revisions is an explicit, versioned object called **Imp**.
FRM rewrites Imp, including the part of Imp that does the rewriting.

> **Start here.** The synthesis paper,
> [*Reach, Not Judgement*](papers/FRM_Synthesis_Reach_Not_Judgement_v1.0.pdf),
> covers the whole programme in 23 pages. The individual studies are below.
> Per-seed result tables are in [`data/`](data/) as CSV files, with a script
> that recomputes the papers' statistics.

## In one paragraph

FRM met every clause of the Level-4 definition, yet five successive
preregistered tests found no causal benefit from rewriting its improvement
mechanism. Measuring the system layer by layer showed why: everything the
mechanism could rewrite was worth about 1.7 percentage points (pp), while the
headroom lay in the form of the policy it learns. When that structure became
rewritable (FELIX-C9), the system's own validation found and adopted a
structural change, and the preregistered causal criteria were met for the
first time: +2.57 pp against the default mechanism (p = 0.0028) and +3.52 pp
against random rewriting (p = 0.0011). The gain held only in distribution: it
was absent on held-out task families and on real bugs. Separately, what the
improvement loop learns transfers to real bugs, replicated three times.

### Names used here

| Name | Meaning |
|---|---|
| **FRM** | Felix Runtime Module, the self-improving system this repository is about |
| **FELIX-C3** | The frozen build of FRM tested in the Stage 3 (Level-4) paper |
| **FELIX-C7** | The study that tests FELIX-C3's policies on real bugs |
| **FELIX-C9** | The study in which the mechanism's structure became rewritable |
| **Imp** | The improvement mechanism: the versioned object that FRM rewrites |
| **C6, C6f, C6r** | Stage 3 conditions: Imp rewritable, Imp frozen, rewrites adopted by coin flip |
| **E, D, R, T** | C9 arms: evolved Imp, default Imp, evidence-free random rewriting, and the designer's best setting (reported only) |
| **FELIX v4** | An earlier, separate system (a population of artificial organisms), described in the May 2026 preprint |

## Papers

| Paper | Date | Pages | Read here | Source |
|---|---|---|---|---|
| **Reach, Not Judgement: What Nine Preregistered Studies Show About When Self-Modification Pays Off** (synthesis) | Oct 2026, v1.0 | 23 | [PDF](papers/FRM_Synthesis_Reach_Not_Judgement_v1.0.pdf) | This repository; not yet on Zenodo or arXiv |
| Rewriting the Structure of Its Own Improvement Mechanism: A Preregistered Causal Test of Bounded Recursive Self-Improvement (FELIX-C9) | Oct 2026, v1.1 | 23 | [PDF](papers/FELIX-C9_Structural_Self-Modification_Preregistered_Test_v1.1.pdf) | This repository; not yet on Zenodo or arXiv |
| Level-4 Bounded Recursive Self-Improvement under a Published Definition: A Preregistered Test of a Self-Referential Improvement Mechanism (FELIX-C3) | Oct 2026, v1.3 | 47 | [PDF](papers/FELIX-C3_Level_4_RSI_Preregistered_Test_v1.3.pdf) | [Zenodo](https://zenodo.org/records/23366534) · DOI [10.5281/zenodo.23366534](https://doi.org/10.5281/zenodo.23366534) |
| Do Self-Improved Repair Policies Transfer to Real Bugs? A Preregistered External-Benchmark Test of a Level-4 Bounded Self-Improving System (FELIX-C7) | Oct 2026, v1.1 | 23 | [PDF](papers/FELIX-C7_External_Benchmark_Transfer_v1.1.pdf) | [Zenodo](https://zenodo.org/records/23366502) · DOI [10.5281/zenodo.23366502](https://doi.org/10.5281/zenodo.23366502) |
| FELIX: A Self-Evolving Organism Demonstrating Reproducible Recursive Self-Improvement via Intergenerational Metabolic Selection | May 2026, v1.0 | 12 | [PDF](papers/earlier/FELIX-v4_Self-Evolving_Organism_RSI_v1.0.pdf) | [Zenodo](https://zenodo.org/records/20156848) · DOI [10.5281/zenodo.20156848](https://doi.org/10.5281/zenodo.20156848) |

All five papers are preprints and have not been peer reviewed. The
[`papers/`](papers/) folder holds every PDF; its [`README.md`](papers/README.md)
lists each file's source, version notes and SHA-256 checksum.

## Key results

### The programme (synthesis)

| Study | Question | Primary result | Verdict |
|---|---|---|---|
| v1 | Does a writable generator beat a fixed one? | +5.2 pp, 24/24 seeds | PASS |
| v2 | Does a self-extending vocabulary beat the designer's? | +4.1 pp, 22/24 | PASS |
| v3 (Stage 3) | Level-4 clauses; does rewriting Imp help? | Clauses met; +0.35 pp, p = 0.23 | Definitional PASS; causal FAIL |
| C3T | Are evolved mechanisms better starting points? | +0.49 pp, p = 0.17 | FAIL |
| v4 | Within-mission validation of rewrites | Pilot −1.04 pp; power 0.00 | Stopped at Gate 1 |
| v5 | Cross-mission validation | Pilot +0.70 pp; power 0.15 | Stopped at Gate 1 |
| v6 | Noise-aware two-stage validation | −1.12 pp, p = 0.97 | FAIL |
| v7 (FELIX-C7) | Do self-improved policies repair real bugs? | +4.85 bugs, 23/24, p = 3 × 10⁻⁷ | PASS |
| v9 (FELIX-C9) | Does rewriting Imp's structure help? | +2.57 pp, p = 0.0028; +3.52 pp vs random | PASS (in distribution) |

The synthesis's conclusion: productive self-modification was limited by what
the system could change (reach), not by how well it judged its changes, and
its benefits stayed in distribution.

### Stage 3: the Level-4 test (FELIX-C3)

The definition, criteria, seeds and gates were registered before any code was
written. The build was frozen and hashed, and the confirmatory experiment ran
once: 24 unused seeds, 3 conditions, 32 rounds per mission.

| Result | Value |
|---|---|
| Classification | Level 4 (definitional): all five definitional criteria pass |
| Missions that promoted audited revisions | 24 / 24 |
| Missions that adopted a validated Imp rewrite | 21 / 24 (60 of 166 trials) |
| Missions where a rewrite changed the rewriting procedure | 17 / 24 |
| Test solve rate, round 0 → round 32 | 27.4% → 40.1% |
| Second-half progress | +2.1 pp, p = 7.6 × 10⁻⁶ |
| Autonomy | 72 / 72 missions with zero interventions; 14 / 14 fault groups; 8 / 8 broken supervisors detected |
| Causal criteria | **Not met**: rewriting vs. frozen Imp +0.35 pp (p = 0.23); vs. random adoption +0.72 pp (p = 0.079) |

The system met the definition, but rewriting its mechanism did not cause its
progress. Four follow-up studies (C3T, v4, v5, v6) did not change that. C9,
below, is the first study that did.

### Transfer to real bugs (FELIX-C7)

The 72 end-state policies from the Stage 3 missions were run, unmodified, on
164 real bugs from QuixBugs and HumanEvalFix.

| Result | Value |
|---|---|
| Real bugs solved, starting policy → self-improved | 21.0 → 25.8 (+4.85, 95% CI [3.80, 5.84]) |
| Relative gain | +23% (vs. +47% on the synthetic domain) |
| Significance | 23 of 24 seeds improved, p = 3.0 × 10⁻⁷ |
| Difference between conditions | None (C6 − C6f +0.26, p = 0.68; C6 − C6r −0.67, p = 0.35) |
| Replications | +4.8 to +5.3 bugs (v6 end states); +4.2 to +4.6 bugs (C9 end states) |

What transfers is the product of the improvement loop. Rewriting the
mechanism has never added a significant real-bug gain.

### Structural self-modification (FELIX-C9)

The mechanism gained a structural gene that selects how evidence becomes a
policy: the default linear learner, three linear variants known from
development to be neutral or harmful, or a tree-ensemble form. Two
independent campaigns proposed, validated and adopted rewrites by the
system's own procedure; the confirmatory run then compared arms on 24 fresh
seeds (7901–7924).

| Contrast | Result |
|---|---|
| **B-1** evolved − default (E − D) | **+2.57 pp** [0.91, 4.17], 18/6, p = 0.0028 ✓ |
| **B-2** evolved − random rewriting (E − R) | **+3.52 pp** [1.84, 5.29], 15/7/2, p = 0.0011 ✓ |
| Campaign 0 seeds (adopted the tree form) | +5.70 pp, 12/0 |
| Campaign 1 seeds (never sampled it) | −0.57 pp, 6/6 |
| Held-out families, E − D | +0.26 pp (not significant) |
| Real bugs, E − D | +0.39 bugs, p = 0.52 |

Every preregistered criterion was met. The paper states three limits: the
useful structure was selected from a designer-supplied menu, not invented;
the result rests on one of two campaigns; and the gain does not extend to
held-out families or real bugs. A post-hoc analysis finds that no policy form
transfers more than about 5 pp to unseen families, which places the limit in
what the system observes.

### Follow-up test T1: the loop against outside baselines

An independent follow-up registered in this repository
([`protocols/`](protocols/)) asked whether the improvement loop beats simple
search at the same budget. On 24 fresh seeds, the loop (Stage 3 condition
C6f) reached 39.6% against 28.2% for evidence-free random search and 27.4%
for a (1+8) evolution strategy: +11.4 and +12.2 pp, 24/24 seeds each,
p = 6 × 10⁻⁸. The baselines spent more evaluations than the loop. Follow-up
T2 is paused part-way and T3 has not been run; see
[`protocols/README.md`](protocols/README.md).

### Earlier work: FELIX v4 organism (May 2026)

> **How to read this paper.** FELIX v4 is exploratory work that came before
> the preregistered programme. It was not preregistered. It reports 5 runs,
> each starting from a population of 4 organisms, has no control condition and no
> statistical tests, and measures each generation by its single best
> organism. It is kept here for completeness and history. The preregistered
> studies above supersede it as evidence about recursive self-improvement.

This earlier preprint describes a different system: a population of artificial
organisms. Each organism mutates its own structure, reproduces when its energy
allows, and passes structure on to other organisms. Fitness is metabolic
efficiency, the reduction in prediction loss per unit of energy spent. Five
runs were made on five seeds (1, 7, 13, 42, 99), each lasting 380 steps, in a
two-stage synthetic environment.

| Result | Value |
|---|---|
| Runs with a full positive chain, Gen 0 → Gen 1 → Gen 2 | 5 / 5 |
| Sustained fitness, Gen 0 → Gen 1 → Gen 2 (mean) | 0.547 → 0.830 → 1.248 |
| Improvement Gen 0 → Gen 2 | +129.7% mean (range +86.3% to +188.0%) |

The paper states its own limits: synthetic data only, a chain three
generations deep, a single laptop, and no released code. It does not claim
that FELIX v4 is general intelligence.

## Repository layout

```
.
├── .github/workflows/
│   └── check-papers.yml          # verifies checksums, listings and statistics
├── papers/
│   ├── README.md                 # sources, versions and checksums
│   ├── SHA256SUMS
│   ├── FRM_Synthesis_Reach_Not_Judgement_v1.0.pdf
│   ├── FELIX-C9_Structural_Self-Modification_Preregistered_Test_v1.1.pdf
│   ├── FELIX-C3_Level_4_RSI_Preregistered_Test_v1.3.pdf
│   ├── FELIX-C7_External_Benchmark_Transfer_v1.1.pdf
│   └── earlier/
│       └── FELIX-v4_Self-Evolving_Organism_RSI_v1.0.pdf   # exploratory work before the programme
├── data/
│   ├── README.md                 # sources, columns and how to verify
│   ├── frmstats.py               # exact Wilcoxon and bootstrap (stdlib only)
│   ├── verify.py                 # recomputes the papers' statistics
│   ├── felix-c3_per_seed_test_solve.csv
│   ├── felix-c3_gate1_pilot.csv
│   ├── felix-c7_per_seed_bugs_solved.csv
│   ├── felix-c9_per_seed.csv
│   └── felix-v4_generational_fitness.csv
├── protocols/
│   ├── README.md                 # status and results of follow-up tests T1–T3
│   ├── OSF_REGISTRATION_TEMPLATE.md   # how to register future studies publicly
│   ├── PREREGISTRATION.md        # the registered protocol (commit 4908d9b)
│   ├── freeze/, results/         # freeze records; T1 results
│   ├── analyze.py, power.py      # decision rules; power analysis
│   └── power_results.txt, results_template.csv
├── .zenodo.json                  # metadata for Zenodo releases
├── CITATION.cff
├── LICENSE
└── README.md
```

## Disclosure and reproducibility

The papers describe FRM in terms of its roles and interfaces. The policy's
features and vocabulary, how linear revisions are constructed, and the
generator are withheld. C9 discloses the policy form it changed.

What you can check here:

- **The papers are authentic.** The C3, C7 and v4 PDFs are byte-identical to
  their copies on Zenodo: each MD5 matches the checksum Zenodo publishes. The
  synthesis and C9 PDFs are the author's release files and are not yet
  deposited elsewhere. Every SHA-256 is in [`papers/SHA256SUMS`](papers/SHA256SUMS).
- **The statistics follow from the printed tables.**
  [`data/verify.py`](data/verify.py) recomputes the reported means, seed counts
  and exact Wilcoxon p-values from the per-seed CSVs of C3, C7 and C9.
- **Follow-up test T1** is registered here, with its freeze records written
  before its missions ran.

What you cannot check here:

- **Mission records, frozen sources and raw result files.** These are in
  confidential audit packages, available to reviewers on request under a
  confidentiality agreement. The papers list the SHA-256 of each one.
- **The registration records of the papers' studies.** Their protocols and
  freeze, gate and results records were registered in a private document
  store with server timestamps, not on a public registry.

The source code is not part of this repository.

The study design, implementation, analysis and drafting were carried out with
substantial assistance from an AI system (Claude, Anthropic) under the author's
direction. The AI is not part of any system under test. See §17.5 of the C3
paper, §11 of the C7 and C9 papers, and §14 of the synthesis.

## Version history

| Paper | Version | Changes |
|---|---|---|
| FELIX-C3 | 1.0 | First public release (Zenodo record 23138422, 4 October 2026). |
| FELIX-C3 | 1.1 | Intermediate revision. Version 1.3 does not list its changes. |
| FELIX-C3 | 1.2 | Added the statement on AI assistance. |
| FELIX-C3 | 1.3 | Added four follow-up studies (transplant test and three redesigns of the rewriter) and a summary of the transfer study. |
| FELIX-C7 | 1.0 | Primary analysis and secondaries S1–S6. Not released publicly. |
| FELIX-C7 | 1.1 | Added S7, the conditional replication on a later study's 72 end states. Nothing else changed. |
| FELIX-C9 | 1.0 | Primary results. Not released publicly. |
| FELIX-C9 | 1.1 | Added §8.3 (post-hoc: why the gain does not generalise) and Figure 5. |
| Synthesis | 1.0 | First release. |
| FELIX v4 | 1.0 | First release (Zenodo record 20156848). |

## Citation

Citation metadata is in [`CITATION.cff`](CITATION.cff). On GitHub, use the
**Cite this repository** button in the sidebar.

The repository itself is archived on Zenodo with each GitHub release. Its
concept DOI, [10.5281/zenodo.23366848](https://doi.org/10.5281/zenodo.23366848),
always resolves to the latest release. To cite a paper, use the paper's own
DOI where it has one. The synthesis and C9 papers do not yet have DOIs; cite
them as preprints until they do.

```bibtex
@misc{felix2026synthesis,
  author = {Felix, Junai P.},
  title  = {Reach, Not Judgement: What Nine Preregistered Studies Show About
            When Self-Modification Pays Off},
  year   = {2026},
  month  = oct,
  note   = {Preprint, version 1.0},
  url    = {https://github.com/recurse-root/FRMDevelopment}
}

@misc{felix2026structural,
  author = {Felix, Junai P.},
  title  = {Rewriting the Structure of Its Own Improvement Mechanism:
            A Preregistered Causal Test of Bounded Recursive Self-Improvement},
  year   = {2026},
  month  = oct,
  note   = {Preprint, version 1.1},
  url    = {https://github.com/recurse-root/FRMDevelopment}
}

@misc{felix2026level4,
  author    = {Felix, Junai P.},
  title     = {Level-4 Bounded Recursive Self-Improvement under a Published Definition:
               A Preregistered Test of a Self-Referential Improvement Mechanism},
  year      = {2026},
  month     = oct,
  publisher = {Zenodo},
  version   = {1.3},
  doi       = {10.5281/zenodo.23366534},
  url       = {https://zenodo.org/records/23366534}
}

@misc{felix2026transfer,
  author    = {Felix, Junai P.},
  title     = {Do Self-Improved Repair Policies Transfer to Real Bugs?
               A Preregistered External-Benchmark Test of a Level-4 Bounded Self-Improving System},
  year      = {2026},
  month     = oct,
  publisher = {Zenodo},
  version   = {1.1},
  doi       = {10.5281/zenodo.23366502},
  url       = {https://zenodo.org/records/23366502}
}

@misc{felix2026organism,
  author    = {Felix, Junai P.},
  title     = {FELIX: A Self-Evolving Organism Demonstrating Reproducible Recursive
               Self-Improvement via Intergenerational Metabolic Selection},
  year      = {2026},
  month     = may,
  publisher = {Zenodo},
  doi       = {10.5281/zenodo.20156848},
  url       = {https://zenodo.org/records/20156848}
}
```

## License

The papers and other contents of this repository are licensed under the
[Creative Commons Attribution 4.0 International License](LICENSE) (CC BY 4.0),
the same license as the Zenodo records. You may share and adapt the material
if you give appropriate credit. Third-party works cited in the papers, such as
QuixBugs and HumanEvalFix, remain under their own licenses.

## Contact

Junai P. Felix, Independent Researcher, Taipei, Taiwan
[junai.felixx@gmail.com](mailto:junai.felixx@gmail.com) · ORCID [0009-0006-1641-0399](https://orcid.org/0009-0006-1641-0399)

The same author appears as *Junai Philip Felix* on Zenodo and as *Junai Felix*
in the FELIX v4 paper.
