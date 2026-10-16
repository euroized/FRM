#!/usr/bin/env bash
# Build the manuscript and the arXiv upload. Run from the repository root:
#   bash arxiv/build.sh
# Needs Python 3 with matplotlib, and a TeX Live with latexmk.
set -euo pipefail
cd "$(dirname "$0")/.."
python3 arxiv/make_figures.py
(cd arxiv && latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex >/dev/null)
tar -czf arxiv/arxiv-submission.tar.gz -C arxiv main.tex figures
echo "Built arxiv/main.pdf and arxiv/arxiv-submission.tar.gz"
