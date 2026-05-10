# Lab 25.1 — Simplest Code
# PS Description

# This program simulates multiple bids and prints the highest bid value.


n = int(input())

bids = []

for i in range(n):

    bids.append(int(input()))

print("Highest Bid =", max(bids))