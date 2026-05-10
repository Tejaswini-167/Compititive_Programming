# LAB 4.1 - Team Selection Count

# Problem Statement:
# A company has n employees and wants to form
# a team of exactly k members.
#
# The order of selection does not matter.

# Formula:

#            n!
#   nCk = ---------
#         k!(n-k)!

# Calculate the total number of distinct
# teams that can be formed.


n, k = map(int, input().split())

result = 1

if k > n:
    print(0)

else:
    for i in range(k):

        result = result * (n - i)
        result = result // (i + 1)

    print(result)

# Input:
# 5 2
#
# Output:
# 10