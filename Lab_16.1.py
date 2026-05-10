# Lab 16.1 — Highest Bid and Next Highest Bid
# PS Description

# This program stores auction bids in a priority queue and prints the highest bid. After removing the highest bid, it prints the next highest bid.

# Input Format
# N
# bid values

# Example:

# 6
# 1200 4500 3200 5100 2800 4000
# Output Format
# Highest Bid: 5100
# Next Highest Bid: 4500
# Simplest Code
import heapq

n = int(input())

bids = list(map(int, input().split()))
pq = []
for b in bids:
    heapq.heappush(pq, -b)

highest = -heapq.heappop(pq)
print("Highest Bid:", highest)
if pq:
    print("Next Highest Bid:", -heapq.heappop(pq))


# YES. Much simpler.

# You do NOT need heap for exam unless sir strictly checks priority queue implementation.

# Simplest Version — 16.1
n = int(input())

bids = list(map(int, input().split()))
bids.sort()
print("Highest Bid:", bids[-1])
print("Next Highest Bid:", bids[-2])