"""Statistics shared by data/verify.py and the protocol scripts.

Standard library only. The exact Wilcoxon signed-rank test follows Appendix C
of the FELIX-C3 paper: zero differences are dropped, tied absolute differences
get midranks, and the null distribution of the doubled signed-rank statistic
is computed exactly.
"""
import random


def mean(xs):
    return sum(xs) / len(xs)


def wilcoxon_upper(diffs):
    """One-sided exact p-value P(W+ >= observed) for H1: median > 0."""
    d = [x for x in diffs if x != 0]
    n = len(d)
    order = sorted(range(n), key=lambda i: abs(d[i]))
    ranks2 = [0] * n  # doubled midranks, always integers
    i = 0
    while i < n:
        j = i
        while j + 1 < n and abs(d[order[j + 1]]) == abs(d[order[i]]):
            j += 1
        for k in range(i, j + 1):
            ranks2[order[k]] = i + j + 2  # 2 * midrank of positions i..j (1-based)
        i = j + 1
    w_obs = sum(r for r, x in zip(ranks2, d) if x > 0)
    counts = {0: 1}
    for r in ranks2:
        nxt = dict(counts)
        for s, c in counts.items():
            nxt[s + r] = nxt.get(s + r, 0) + c
        counts = nxt
    return sum(c for s, c in counts.items() if s >= w_obs) / 2 ** n


def wilcoxon_two_sided(diffs):
    up = wilcoxon_upper(diffs)
    down = wilcoxon_upper([-x for x in diffs])
    return min(1.0, 2 * min(up, down))


def signs(diffs):
    return (sum(x > 0 for x in diffs), sum(x < 0 for x in diffs),
            sum(x == 0 for x in diffs))


def bootstrap_ci(xs, b=20000, seed=0, level=0.95):
    """Percentile bootstrap interval of the mean, resampling units."""
    rng = random.Random(seed)
    n = len(xs)
    means = sorted(sum(rng.choice(xs) for _ in range(n)) / n for _ in range(b))
    lo = means[int((1 - level) / 2 * b)]
    hi = means[int((1 + level) / 2 * b) - 1]
    return lo, hi
