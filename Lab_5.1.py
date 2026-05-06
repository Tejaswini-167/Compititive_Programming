# LAB 5.1
# Probability of drawing exactly r cards
# from a specific suit

# Formula:

#  C(s,r) * C(52-s,k-r)
# ----------------------
#         C(52,k)


import math

s = int(input("Enter cards in one suit: "))
k = int(input("Enter number of cards drawn: "))
r = int(input("Enter same suit cards: "))


def ncr(n, r):

    return math.factorial(n) // (
        math.factorial(r) * math.factorial(n - r)
    )


total_cards = 52

favorable = ncr(s, r) * ncr(total_cards - s, k - r)

total = ncr(total_cards, k)

probability = favorable / total

print(probability)


# Input:
# 13
# 5
# 2

# Output:
# 0.274279...