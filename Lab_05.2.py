# LAB 5.2
# Quality Inspection Probability

# Problem Statement:

# A factory manufactures n items.
# Among them, d items are defective.
# From these n items, k items are selected randomly
# for inspection.

# Find the probability that exactly r defective
# items are selected.

# Formula:
#
#  C(d,r) * C(n-d,k-r)
# ---------------------
#        C(n,k)
#
# where:
#
# n = total items
# d = defective items
# k = selected items
# r = defective items selected

import math


def comb(n, r):

    return math.factorial(n) // (
        math.factorial(r) * math.factorial(n - r)
    )


n, d, k, r = map(int, input().split())

favorable = comb(d, r) * comb(n - d, k - r)

total = comb(n, k)

probability = favorable / total

print(round(probability, 6))


# Input:
# 100 10 8 2

# Output:
# 0.150156