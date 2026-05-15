# Lab 16.2 — Highest Bid Using Priority Queue
# PS Description

# This program stores auction bids in a priority queue (max-heap) and prints the highest bid value.

# Input Format
# N
# bid values

import heapq

n = int(input())

bids = list(map(int, input().split()))

pq = []

for b in bids:
    heapq.heappush(pq, -b)

print(-heapq.heappop(pq))