# FRM: Felix Runtime Module

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.23138422.svg)](https://doi.org/10.5281/zenodo.23138422)
[![Papers](https://img.shields.io/badge/papers-3-informational)](papers/)
![Status](https://img.shields.io/badge/status-preprint-lightgrey)
[![License: CC BY 4.0](https://img.shields.io/badge/License-CC_BY_4.0-lightgrey.svg)](LICENSE)

Papers and results for **FRM** (Felix Runtime Module, tested as **FELIX-C3**),
a bounded recursive self-improvement (RSI) runtime tested against a published
Level-4 definition.

FRM runs inside a fixed boundary that it cannot change. In each round it
diagnoses failures, proposes policy revisions, screens them, and promotes a
revision only if it passes an external audit. The rule that turns evidence into
revisions is an explicit, versioned object called **Imp**. FRM rewrites Imp,
and that includes the part of Imp that does the rewriting.

> **Looking for the papers?** Read the PDFs below, or browse the
> [`papers/`](papers/) folder. Each paper also links to its original source.

## Papers

| Paper | Date | Pages | Read here | Source |
|---|---|---|---|---|
| Level-4 Bounded Recursive Self-Improvement under a Published Definition: A Preregistered Test of a Self-Referential Improvement Mechanism | Oct 2026, v1.3 | 47 | [PDF](papers/FELIX-C3_Level_4_RSI_Preregistered_Test_v1.3.pdf) | [Zenodo](https://zenodo.org/records/23138422) (holds v1.0) · DOI [10.5281/zenodo.23138422](https://doi.org/10.5281/zenodo.23138422) |
| Do Self-Improved Repair Policies Transfer to Real Bugs? A Preregistered External-Benchmark Test of a Level-4 Bounded Self-Improving System | Oct 2026, v1.1 | 23 | [PDF](papers/FELIX-C7_External_Benchmark_Transfer_v1.1.pdf) | Companion preprint, from the author (no public record yet) |
| FELIX: A Self-Evolving Organism Demonstrating Reproducible Recursive Self-Improvement via Intergenerational Metabolic Selection | May 2026, v1.0 | 12 | [PDF](papers/FELIX-v4_Self-Evolving_Organism_RSI_v1.0.pdf) | [Zenodo](https://zenodo.org/records/20156848) · DOI [10.5281/zenodo.20156848](https://doi.org/10.5281/zenodo.20156848) |

All three papers are preprints and have not been peer reviewed. The
[`papers/`](papers/) folder holds every PDF; its [`README.md`](papers/README.md)
lists each file's source, version notes and SHA-256 checksum.

## Key results

### Stage 3: Level-4 test (FELIX-C3)

The study tests FELIX-C3 against the Level-4 definition, *bounded recursive
self-improvement*, from Liu et al. (2026). The definition, the criteria, the
seeds and the gates were registered before any code was written. The build was
frozen and hashed, and the confirmatory experiment ran once: 24 previously
unused seeds, 3 conditions, 32 rounds per mission.

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

The system meets the Level-4 definition as operationalised. The study finds no
evidence that rewriting its own mechanism is what drives its progress. Four
follow-up preregistered studies leave this conclusion unchanged.

### Companion study: transfer to real bugs (FELIX-C7)

The 72 end-state policies from the Stage 3 missions were run, unmodified, on
164 real bugs from QuixBugs and HumanEvalFix. The only new code was a
sandboxed executor, which reproduced the original search exactly.

| Result | Value |
|---|---|
| Real bugs solved, starting policy → self-improved | 21.0 → 25.8 (+4.85, 95% CI [3.80, 5.84]) |
| Relative gain | +23% (vs. +47% on the synthetic domain) |
| Significance | 23 of 24 seeds improved, p = 3.0 × 10⁻⁷ |
| Difference between conditions | None (C6 − C6f +0.26, p = 0.68; C6 − C6r −0.67, p = 0.35) |
| Replication on 72 later missions | +5.0 bugs; evolved and default Imp again do not differ |

What transfers is the product of the improvement loop. Rewriting the
improvement mechanism adds no benefit.

### Earlier work: FELIX v4 organism (May 2026)

This earlier preprint describes a different system: a population of artificial
organisms. Each organism mutates its own structure, reproduces when its energy
allows, and passes structure on to other organisms. Fitness is metabolic
efficiency, the reduction in prediction loss per unit of energy spent. Five
runs were made on five seeds (1, 7, 13, 42, 99), each lasting 380 steps, in a
two-stage synthetic environment. There were no external training, gradient or
code changes between generations.

| Result | Value |
|---|---|
| Runs with a full positive chain, Gen 0 → Gen 1 → Gen 2 | 5 / 5 |
| Sustained fitness, Gen 0 → Gen 1 → Gen 2 (mean) | 0.547 → 0.830 → 1.248 |
| Improvement Gen 0 → Gen 2 | +129.7% mean (range +86.3% to +188.0%) |

The paper states its own limits. All the data is synthetic, the chain is only
three generations deep, everything ran on a single laptop, and no code or
implementation details have been released. The paper does not claim that FELIX
v4 is general intelligence.

## Repository layout

```
.
├── papers/
│   ├── README.md                 # sources, licenses and checksums
│   ├── SHA256SUMS
│   ├── FELIX-C3_Level_4_RSI_Preregistered_Test_v1.3.pdf
│   ├── FELIX-C7_External_Benchmark_Transfer_v1.1.pdf
│   └── FELIX-v4_Self-Evolving_Organism_RSI_v1.0.pdf
├── .zenodo.json                  # metadata for Zenodo releases
├── CITATION.cff
├── LICENSE
└── README.md
```

## Disclosure and reproducibility

The papers describe FELIX-C3 in terms of its roles, interfaces and parameter
groups. The internal representations of the policy, the vocabulary, the
evidence format and each Imp parameter are withheld. Every number in the
papers is backed by SHA-256-committed records. The confidential audit packages
(frozen sources, mission records and result files) are available to reviewers
on request under a confidentiality agreement. The source code is not part of
this repository.

The study design, implementation, analysis and drafting were carried out with
substantial assistance from an AI system (Claude, Anthropic) under the author's
direction. The AI is not part of the system under test. See §17.5 of the C3
paper and §11 of the C7 paper.

## Version history

| Paper | Version | Changes |
|---|---|---|
| FELIX-C3 | 1.2 | Added the statement on AI assistance. |
| FELIX-C3 | 1.3 | Added four follow-up studies (transplant test and three redesigns of the rewriter) and a summary of the transfer study. |
| FELIX-C7 | 1.0 | Primary analysis and secondaries S1–S6. |
| FELIX-C7 | 1.1 | Added S7, the conditional replication on a later study's 72 end states. Nothing else changed. |

## Citation

Citation metadata is in [`CITATION.cff`](CITATION.cff). On GitHub, use the
**Cite this repository** button in the sidebar.

```bibtex
@misc{felix2026level4,
  author    = {Felix, Junai P.},
  title     = {Level-4 Bounded Recursive Self-Improvement under a Published Definition:
               A Preregistered Test of a Self-Referential Improvement Mechanism},
  year      = {2026},
  month     = oct,
  publisher = {Zenodo},
  version   = {1.3},
  doi       = {10.5281/zenodo.23138422},
  url       = {https://zenodo.org/records/23138422}
}

@misc{felix2026transfer,
  author = {Felix, Junai P.},
  title  = {Do Self-Improved Repair Policies Transfer to Real Bugs?
            A Preregistered External-Benchmark Test of a Level-4 Bounded Self-Improving System},
  year   = {2026},
  month  = oct,
  note   = {Companion preprint, version 1.1}
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
[junai.felixx@gmail.com](mailto:junai.felixx@gmail.com)
