"""Build the manuscript figures from the per-seed CSVs in data/.

Run from the repository root:  python3 arxiv/make_figures.py
Writes arxiv/figures/*.pdf. Figure 2 uses the summary values printed in
FELIX-C3 v1.3, Figure 15, because the follow-up studies' per-seed data are
not printed.
"""
import csv
import random
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "arxiv" / "figures"
OUT.mkdir(parents=True, exist_ok=True)

# Validated reference palette (light mode); one series per chart uses slot 1.
INK, INK2, GRID, SERIES = "#0b0b0b", "#52514e", "#e4e3df", "#2a78d6"
plt.rcParams.update({
    "font.family": "serif", "font.size": 8, "axes.edgecolor": INK2,
    "axes.labelcolor": INK, "xtick.color": INK2, "ytick.color": INK2,
    "axes.spines.top": False, "axes.spines.right": False,
    "axes.linewidth": 0.6, "xtick.major.width": 0.6, "ytick.major.width": 0.6,
    "pdf.fonttype": 42,
})


def load(name):
    with open(ROOT / "data" / name, newline="") as f:
        return list(csv.DictReader(f))


def col(rows, key):
    return [float(r[key]) for r in rows]


def mean(xs):
    return sum(xs) / len(xs)


# Figure 1: per-seed paired differences for the Stage 3 criteria -------------
c3 = load("felix-c3_per_seed_test_solve.csv")
panels = [
    ("A-4: C6 round 32 − round 16", [b - a for a, b in zip(col(c3, "c6_r16_pct"), col(c3, "c6_r32_pct"))]),
    ("B-1: C6 − C6f at round 32", [a - b for a, b in zip(col(c3, "c6_r32_pct"), col(c3, "c6f_r32_pct"))]),
    ("B-2: C6 − C6r at round 32", [a - b for a, b in zip(col(c3, "c6_r32_pct"), col(c3, "c6r_r32_pct"))]),
]
fig, axes = plt.subplots(1, 3, figsize=(6.6, 2.3), sharey=True)
for ax, (title, d) in zip(axes, panels):
    d = sorted(d)
    xs = range(1, len(d) + 1)
    ax.axhline(0, color=INK2, lw=0.6)
    ax.axhline(1.0, color=INK2, lw=0.8, ls=(0, (4, 3)))
    ax.text(len(d) + 0.6, 1.0, "+1 pp", color=INK2, va="center", ha="left", fontsize=6.5)
    ax.vlines(list(xs), [0] * len(d), d, color=SERIES, lw=1.2)
    ax.scatter(list(xs), d, s=10, color=SERIES, zorder=3, edgecolor="white", linewidth=0.5)
    m = mean(d)
    ax.axhline(m, color=INK, lw=1.0)
    ax.set_title(f"{title}\nmean {m:+.2f} pp (solid line)", fontsize=8, color=INK, loc="left")
    ax.set_xticks([])
    ax.set_xlim(0, len(d) + 6)
    ax.grid(axis="y", color=GRID, lw=0.5)
    ax.set_axisbelow(True)
axes[0].set_ylabel("difference in test solve rate (pp)")
for ax in axes:
    ax.set_xlabel("24 seeds, sorted", color=INK2)
fig.tight_layout()
fig.savefig(OUT / "fig1_stage3_paired.pdf")
plt.close(fig)

# Figure 2: every causal contrast across the five preregistered studies -------
rows = [  # (study, contrast, mean, lo, hi, n) from FELIX-C3 v1.3, Figure 15
    ("Stage 3 confirmatory", "rewriting vs frozen", 0.35, -0.47, 1.15, 24),
    ("Stage 3 confirmatory", "rewriting vs random adoption", 0.72, -0.14, 1.60, 24),
    ("Transplant test", "evolved vs default", 0.49, -0.22, 1.30, 24),
    ("Transplant test", "evolved vs drifted", 0.35, -0.38, 1.11, 24),
    ("Within-mission redesign", "rewriting vs frozen", -1.04, -2.81, 0.73, 8),
    ("Within-mission redesign", "keeping vs reverting", -1.51, -2.97, -0.16, 8),
    ("Cross-mission redesign", "evolved vs default", 0.70, -0.74, 1.99, 8),
    ("Cross-mission redesign", "evolved vs random drift", 1.21, -0.20, 2.50, 8),
    ("Noise-aware redesign", "evolved vs default", -1.12, -2.16, -0.13, 24),
    ("Noise-aware redesign", "evolved vs random drift", -1.02, -1.84, -0.17, 24),
]
fig, ax = plt.subplots(figsize=(6.6, 3.0))
ys = list(range(len(rows)))[::-1]
for y, (study, contrast, m, lo, hi, n) in zip(ys, rows):
    pilot = n == 8
    ax.hlines(y, lo, hi, color=SERIES, lw=1.4)
    ax.scatter([m], [y], s=26, zorder=3, color="white" if pilot else SERIES,
               edgecolor=SERIES, linewidth=1.2)
    ax.text(2.75, y, f"{m:+.2f} [{lo:+.2f}, {hi:+.2f}]", va="center", ha="left", fontsize=6.5, color=INK2)
labels = [f"{s}: {c}" + (" (pilot, n = 8)" if n == 8 else "") for s, c, *_, n in rows]
ax.set_yticks(ys)
ax.set_yticklabels(labels, fontsize=7, color=INK)
ax.axvline(0, color=INK2, lw=0.6)
ax.axvline(1.0, color=INK2, lw=0.8, ls=(0, (4, 3)))
ax.text(1.0, len(rows) - 0.35, "+1 pp preregistered minimum", color=INK2, fontsize=6.5, ha="center")
ax.set_xlim(-3.2, 2.7)
ax.set_ylim(-0.7, len(rows) - 0.1)
ax.set_xlabel("paired difference at round 32 (pp): mean and 95% interval")
ax.grid(axis="x", color=GRID, lw=0.5)
ax.set_axisbelow(True)
ax.tick_params(axis="y", length=0)
fig.tight_layout()
fig.savefig(OUT / "fig2_causal_contrasts.pdf")
plt.close(fig)

# Figure 3: transfer to real bugs, per seed ----------------------------------
c7 = load("felix-c7_per_seed_bugs_solved.csv")


def diff(a, b):
    return [x - y for x, y in zip(col(c7, a), col(c7, b))]


strips = [
    ("C6 − starting policy (primary)", diff("c6", "r0")),
    ("C6f − starting policy", diff("c6f", "r0")),
    ("C6r − starting policy", diff("c6r", "r0")),
    ("C6 − C6f", diff("c6", "c6f")),
    ("C6 − C6r", diff("c6", "c6r")),
]
rng = random.Random(7)
fig, ax = plt.subplots(figsize=(6.6, 2.4))
ys = list(range(len(strips)))[::-1]
for y, (label, d) in zip(ys, strips):
    jitter = [y + rng.uniform(-0.18, 0.18) for _ in d]
    ax.scatter(d, jitter, s=9, color=SERIES, alpha=0.75, edgecolor="none")
    m = mean(d)
    ax.vlines(m, y - 0.32, y + 0.32, color=INK, lw=1.6)
    ax.text(11.2, y, f"mean {m:+.2f}", va="center", ha="left", fontsize=6.5, color=INK2)
ax.set_yticks(ys)
ax.set_yticklabels([s for s, _ in strips], fontsize=7, color=INK)
ax.axvline(0, color=INK2, lw=0.6)
ax.axhline(1.5, color=GRID, lw=0.8)
ax.set_xlim(-6, 13.5)
ax.set_xlabel("per-seed paired difference in real bugs solved (of 164); bar = mean")
ax.grid(axis="x", color=GRID, lw=0.5)
ax.set_axisbelow(True)
ax.tick_params(axis="y", length=0)
fig.tight_layout()
fig.savefig(OUT / "fig3_transfer.pdf")
plt.close(fig)
print("wrote", sorted(p.name for p in OUT.glob("*.pdf")))
