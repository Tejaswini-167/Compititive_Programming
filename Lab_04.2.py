# LAB 4.2 - Possible Hands Count

# Problem Statement:
# In a card game, a player is dealt exactly
# K cards from a deck containing N distinct cards.

# The order of cards does not matter.

# Formula:

#            N!
#   nCk = ---------
#         K!(N-K)!

# Calculate the total number of possible hands.

def factorial(n):

    fact = 1

    for i in range(1, n + 1):
        fact = fact * i

    return fact

N, K = map(int, input().split())
result = factorial(N) // (factorial(K) * factorial(N - K))
print(result)


# Input:
# n value: 5
# k value: 2

# Output:
# 10