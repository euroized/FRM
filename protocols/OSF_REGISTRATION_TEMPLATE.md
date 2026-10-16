# OSF preregistration template for future FRM studies

Earlier studies in this programme were registered in a private document store
with server timestamps. Future studies should also be registered on the Open
Science Framework (OSF), which gives an independent, public, time-stamped
record that cannot be edited after submission.

This template follows the sections of the OSF Preregistration form. Copy it
into a new registration, replace every `<…>`, and keep the defaults unless the
study gives a reason to change them; record any change under *Deviations*.
It contains no system internals: describe the system at the level of roles
and interfaces, as the papers do.

## How to register

1. Create a free account at [osf.io](https://osf.io) and a new project for the
   study (for example "FRM study vN").
2. Upload the protocol (this filled-in template) and, once it exists, the
   freeze record's SHA-256. Do not upload source code.
3. Choose **Registrations → New registration → OSF Preregistration**, paste
   the sections below, and submit. Choose an embargo (up to four years) if the
   design must stay private until the results are out; the timestamp is fixed
   either way.
4. Put the registration DOI in the study's freeze record and paper, and add it
   to [`README.md`](README.md) in this folder.
5. Register before any code for the study is written, as the programme's
   protocols require, or at the latest before the freeze. Only then run Gate 0.

## Study information

- **Title:** `<FRM study vN: question in one line>`
- **Authors:** Junai P. Felix (Independent Researcher, Taipei, Taiwan)
- **Research question:** `<the causal or descriptive question>`
- **Hypotheses:** `<directional hypotheses, one per primary criterion>`

## Design plan

- **Study type:** Experiment. Computational, fully seeded, deterministic.
- **Blinding:** Not applicable (automated pipeline). Analysis is fixed in code
  before any confirmatory run and applied without inspection of results.
- **Arms** (paired on the same seeds under common random numbers):
  - `E`: `<system with the manipulated component>`
  - `D`: `<frozen or default system>`
  - `R`: `<evidence-free control: the same proposal process, adopting the same
    number of changes at random, regardless of evidence>`
  - `<optional arms, marked "reported only">`
- **Randomisation:** Seeds are assigned in advance; all arms share each seed.

## Sampling plan

- **Seeds:** confirmatory `<range, never used before>`; pilot `<range>`;
  development `<range>`. List every previously used range and confirm no
  overlap.
- **Sample size:** `<n>` seeds, justified by a power analysis from a pilot
  (bootstrap of pilot paired differences, `<B>` resamples) at the decision
  rule below. Report the power estimate before the confirmatory run.
- **Stopping rule:** The confirmatory runs once, on all seeds. No seed is
  dropped and nothing is rerun. Crash-only resume after interruptions is
  allowed and every interruption is logged.

## Variables

- **Primary outcome:** `<for example, round-32 test solve rate on all 16
  families>`.
- **Secondary outcomes:** held-out task families (fixed by a hash of the
  freeze); real bugs from QuixBugs and HumanEvalFix through the frozen
  companion pipeline; evaluations spent per arm.
- **Integrity variables:** freeze verification, mission reconciliation,
  replay of adaptive decisions, interventions (must be zero).

## Analysis plan

- **Tests:** exact one-sided Wilcoxon signed-rank on the per-seed paired
  differences (zeros dropped, midranks for ties), as in FELIX-C3 Appendix C.
  Secondary and out-of-distribution contrasts two-sided.
- **Intervals:** percentile bootstrap, 20,000 resamples, fixed seed.
- **Decision rules** (unchanged since Stage 3 unless stated):
  - `E − D` mean ≥ +1.0 pp and p < 0.01
  - `E − R` mean ≥ +0.5 pp and p < 0.05
  - `<Tier A / gate criteria>`
- **Gates:** Gate 0 (determinism, crash-only resume, headroom, autonomy
  suite); Gate 1 (power from the pilot, or an adaptation criterion). A failed
  gate stops the study and is reported.
- **Inference criteria:** `<verdict labels and what each requires>`.
- **Exploratory analyses:** listed here in advance where possible; anything
  else is labelled post hoc.

## Other

- **What was known before registration:** `<all development runs and their
  results that shaped the design>`.
- **Stated risks:** `<design risks with their probabilities, computed from the
  frozen code where possible>`.
- **Disclosure boundary:** the system is described by roles and interfaces;
  features, vocabulary, revision construction and the generator are withheld.
  Frozen sources and run records go in a confidential audit package whose
  SHA-256 is published.
- **Deviations:** `<none yet>`
- **AI assistance:** design, implementation, execution, analysis and drafting
  carried out with substantial assistance from an AI system (Claude,
  Anthropic) under the author's direction; the AI is not part of the system
  under test.
