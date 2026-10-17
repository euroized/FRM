# Papers

These are the preprints in this repository, newest first. All are released
under [CC BY 4.0](../LICENSE). Verify the files with `sha256sum -c SHA256SUMS`
from this directory.

| File | Paper | Date | Pages | Source |
|---|---|---|---|---|
| [`FRM_Synthesis_Reach_Not_Judgement_v1.1.pdf`](FRM_Synthesis_Reach_Not_Judgement_v1.1.pdf) | Reach, Not Judgement: What Nine Preregistered Studies Show About When Self-Modification Pays Off | Oct 2026, v1.1 | 23 | [Zenodo 23427841](https://doi.org/10.5281/zenodo.23427841) |
| [`FELIX-C9_Structural_Self-Modification_Preregistered_Test_v1.2.pdf`](FELIX-C9_Structural_Self-Modification_Preregistered_Test_v1.2.pdf) | Rewriting the Structure of Its Own Improvement Mechanism: A Preregistered Causal Test of Bounded Recursive Self-Improvement | Oct 2026, v1.2 | 25 | [Zenodo 23427738](https://doi.org/10.5281/zenodo.23427738) |
| [`FELIX-C3_Level_4_RSI_Preregistered_Test_v1.3.pdf`](FELIX-C3_Level_4_RSI_Preregistered_Test_v1.3.pdf) | Level-4 Bounded Recursive Self-Improvement under a Published Definition: A Preregistered Test of a Self-Referential Improvement Mechanism | Oct 2026, v1.3 | 47 | [Zenodo 23366534](https://doi.org/10.5281/zenodo.23366534) |
| [`FELIX-C7_External_Benchmark_Transfer_v1.1.pdf`](FELIX-C7_External_Benchmark_Transfer_v1.1.pdf) | Do Self-Improved Repair Policies Transfer to Real Bugs? A Preregistered External-Benchmark Test of a Level-4 Bounded Self-Improving System | Oct 2026, v1.1 | 23 | [Zenodo 23366502](https://doi.org/10.5281/zenodo.23366502) |
| [`earlier/FELIX-v4_Self-Evolving_Organism_RSI_v1.0.pdf`](earlier/FELIX-v4_Self-Evolving_Organism_RSI_v1.0.pdf) | FELIX: A Self-Evolving Organism Demonstrating Reproducible Recursive Self-Improvement via Intergenerational Metabolic Selection | May 2026, v1.0 | 12 | [Zenodo 20156848](https://doi.org/10.5281/zenodo.20156848) |

## SHA-256

| File | SHA-256 |
|---|---|
| `FRM_Synthesis_Reach_Not_Judgement_v1.1.pdf` | `0c9fbbf72b1d28495803d236005d5f369a60e8e425c63281808a5c832c922a4a` |
| `FELIX-C9_Structural_Self-Modification_Preregistered_Test_v1.2.pdf` | `d58d38ec749168a56c2551b022ff590a874ee4276d1808e1d47547620f938711` |
| `FELIX-C3_Level_4_RSI_Preregistered_Test_v1.3.pdf` | `90a0c1789738224a5014b22b3238e9e6fbae2abe7545b1c6a9897c0944d87688` |
| `FELIX-C7_External_Benchmark_Transfer_v1.1.pdf` | `ba6beab19c1f4eec31c1f569806ec68e41ce9b865dec8142d7c6d4f94478f9a9` |
| `earlier/FELIX-v4_Self-Evolving_Organism_RSI_v1.0.pdf` | `fb257a6d5e13349f9583b0bcf139b5ffc50704884fb40a1cd7c73cc739034853` |

## Notes

- **Synthesis v1.1 (Reach, Not Judgement).** Covers all nine preregistered
  studies (v1–v7 and v9): writable generators, the Level-4 test and its five
  null causal tests, real-bug transfer, the bottleneck analysis, the C9
  structural study and the generality limit. It includes a safety and
  containment section. This is the recommended entry point to the programme
  and the intended first arXiv submission. Zenodo record 23427841; this file
  is byte-identical to the Zenodo file. v1.1 adds the independent rerun of v9
  (§14) and small corrections to v1.0.
- **FELIX-C9 v1.2.** The study in which the system's own validated rewrite of
  its improvement mechanism's structure met the preregistered causal criteria
  for the first time (+2.57 pp against the default, p = 0.0028), in
  distribution only. v1.1 added §8.3, a post-hoc analysis of why the gain does
  not generalise. v1.2 adds an independent rerun of the whole frozen protocol,
  which reproduced the structural rewrite exactly and met every criterion again,
  and discloses that the l1 decoy learner was not seeded (§11). Zenodo record
  23427738; this file is byte-identical to the Zenodo file. Its per-seed table
  (unchanged from v1.1) is in
  [`../data/felix-c9_per_seed.csv`](../data/felix-c9_per_seed.csv).
- **FELIX v4 (May 2026), in [`earlier/`](earlier/).** This file is an unmodified copy of the file in
  Zenodo record 20156848. Its MD5, `11c3ba2dc6f6cd52fcd58f0d47d6a3a6`, matches
  the checksum Zenodo publishes for the file. The paper describes a
  population-based organism, a different system from the FELIX-C3 runtime
  module. It is exploratory work that came before the preregistered
  programme. It was not preregistered and has no control condition or
  statistical tests. The Zenodo record has no version number and holds a single version,
  so it is filed here as v1.0. Its own reference [2] cites an earlier FELIX
  preprint, which is not included here.
- **FELIX-C3 v1.3.** This version adds four follow-up studies and a summary of
  the transfer study. It is Zenodo record 23366534, a new version of record
  23138422 (v1.0). The concept DOI 10.5281/zenodo.23138421 always resolves to
  the latest version.
- **FELIX-C7 v1.1.** This version adds secondary analysis S7. It is Zenodo
  record 23366502, the first public version.
