# PS Description

# This program safely processes multiple bids and prints the highest bid value using synchronization concept.

n = int(input())

bids = []

for i in range(n):

    bids.append(int(input()))

print("Highest Bid =", max(bids))