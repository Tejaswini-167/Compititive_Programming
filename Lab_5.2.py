# LAB 5.2
# Quality Inspection Probability

# Formula:

#  C(d,r) * C(n-d,k-r)
# ---------------------
#        C(n,k)

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