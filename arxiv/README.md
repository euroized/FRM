# arXiv manuscript (superseded, do not submit)

> **Superseded.** This draft predates the FELIX-C9 study. Its central claim,
> that the recursion "contributes nothing measurable", no longer describes the
> programme: in C9 the system's self-rewriting met the preregistered causal
> criteria for the first time (in-distribution only). The paper to submit to
> arXiv is the synthesis,
> [*Reach, Not Judgement*](../papers/FRM_Synthesis_Reach_Not_Judgement_v1.0.pdf).
> This folder is kept only as a record and will be removed.

**Meeting a Definition of Recursive Self-Improvement Is Not Evidence That the
Recursion Helps: A Preregistered Test with Counterfactual Controls**

This manuscript consolidates the FELIX-C3 v1.3 and FELIX-C7 v1.1 preprints for
arXiv. It leads with their central finding: the system meets the Level-4
definition, but its recursion contributes nothing measurable.

**What is new.** The paper adds:
- a reanalysis from the printed per-seed tables (`data/verify.py`)
- a power analysis (`protocols/power.py`)
- a proposed reporting standard for RSI claims
- the follow-up test protocol (`protocols/PREREGISTRATION.md`)

**What is not new.** It reports no new experiments. The follow-up tests are
described as planned and have not been run.

| File | What it is |
|---|---|
| [`main.pdf`](main.pdf) | The compiled manuscript (11 pages, 3 figures) |
| `main.tex` | Source. The bibliography is inline, so no BibTeX run is needed. |
| `figures/` | Figures, built from `data/` by `make_figures.py` |
| `build.sh` | Rebuilds the figures and the PDF, and writes `arxiv-submission.tar.gz` |

## Building

```
bash arxiv/build.sh
```

Building needs Python 3 with matplotlib and a TeX Live with `latexmk`. It
writes `arxiv/arxiv-submission.tar.gz` (`main.tex` and `figures/`), which
is the file to upload. That tarball has been tested to compile from scratch
with pdflatex.

## Submitting

**Before uploading:**
1. Read the PDF end to end and confirm every statement is one you stand
   behind. You are the sole author and responsible for all of it.
2. Make sure the arXiv account uses the same name as the papers. Add an ORCID
   if you have one.
3. A first submission to **cs.AI** needs an endorsement from an established
   arXiv author in that category. arXiv tells you this during submission and
   gives you a code to send to an endorser.

**Submission form:**

| Field | Value |
|---|---|
| Primary category | `cs.AI` (Artificial Intelligence) |
| Cross-lists | `cs.LG`, `cs.SE` |
| License | CC BY 4.0, the same as the Zenodo records |
| Upload | `arxiv-submission.tar.gz` |
| Comments | `11 pages, 3 figures. Consolidates Zenodo preprints 10.5281/zenodo.23366534 and 10.5281/zenodo.23366502. Data and code: https://github.com/recurse-root/FRMDevelopment` |

**Title:**

```
Meeting a Definition of Recursive Self-Improvement Is Not Evidence That the Recursion Helps: A Preregistered Test with Counterfactual Controls
```

**Abstract** (plain text, 1852 characters; arXiv's limit is 1,920):

```
Claims of recursive self-improvement (RSI) are usually judged against criteria their authors choose, and recent capability taxonomies grade systems by which roles they perform. We test whether satisfying such a definition shows that the recursion is productive. A self-modifying program-repair runtime, FELIX-C3, was tested against the published Level-4 definition of bounded RSI of Liu et al. (2026). Its improvement mechanism is an explicit, versioned object that contains the procedure for editing itself. Definition, criteria, seeds and gates were registered before any code was written; the build was frozen and hashed; the confirmatory experiment ran once (24 unused seeds x 3 conditions, 32 rounds, no operator). Every definitional criterion passed: validated rewrites of the mechanism were adopted in 21 of 24 missions, the rewriting procedure rewrote itself in 17, and test solve rate rose from 27.4% to 40.1% with significant second-half progress (p = 7.6e-6). The counterfactual criteria failed: rewriting did not beat the same system with its mechanism frozen (+0.35 pp, p = 0.23) or with rewrites adopted by coin flip (+0.72 pp, p = 0.079). Four further preregistered studies, including a noise-aware redesign whose rewrites did worse than the default (-1.12 pp), did not change this. A companion preregistered study found that the system's policies repair 23% more real bugs from QuixBugs and HumanEvalFix than its starting policy (p = 3.0e-7), equally under all three conditions. A system can therefore meet a Level-4 definition while its recursion contributes nothing measurable. We propose that RSI claims report matched-budget frozen-mechanism and random-adoption controls with a power analysis, and we release per-seed data, a reanalysis that reproduces the reported statistics, and a preregistration draft for three follow-up tests.
```

**After it is announced:** add the arXiv ID to the repository README and to
`CITATION.cff`, and link it from both Zenodo records under "related works".
