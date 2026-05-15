# LAB 5.1  : Probability of Drawing Cards from Same Suit
# Problem Statement:

# A standard deck contains 52 playing cards.
# A suit contains 13 cards
# (Example: Hearts, Spades, Clubs, Diamonds).
# You randomly draw k cards from the deck
# without replacement.
# Find the probability of drawing exactly
# r cards from a specific suit.


def ncr(n, r):
    result = 1

    for i in range(r):
        result = result * (n - i)
        result = result // (i + 1)

    return result

k, r = map(int, input().split())

favorable = ncr(13, r) * ncr(39, k - r)
total = ncr(52, k)
probability = favorable / total
print(f"{probability:.6f}")

