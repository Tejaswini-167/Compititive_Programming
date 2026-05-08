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

n = int(input("Enter n value: "))
k = int(input("Enter k value: "))


def fact(x):

    result = 1

    for i in range(1, x + 1):
        result = result * i

    return result
r = n - k
ans = fact(n) // (fact(k) * fact(r))
print(ans)


# Input:
# n value: 5
# k value: 2

# Output:
# 10