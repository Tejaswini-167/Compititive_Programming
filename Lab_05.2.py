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

def ncr(n, r):
    if r > n:
        return 0
    result = 1

    for i in range(r):
        result = result * (n - i)
        result = result // (i + 1)

    return result

N, D, K, R = map(int, input().split())
favorable = ncr(D, R) * ncr(N - D, K - R)
total = ncr(N, K)
probability = favorable / total
print(f"{probability:.6f}")


# Input:
# 100 10 8 2

# Output:
# 0.150156