# Lab 19.2 — Minimum Cost Between Two Cities
# PS Description

# This program finds the minimum travel cost/path between two cities using Dijkstra algorithm.


import heapq

n, e = map(int, input().split())

graph = [[] for i in range(n)]

for i in range(e):

    u, v, w = map(int, input().split())

    graph[u].append((v, w))
    graph[v].append((u, w))

s, d = map(int, input().split())

dist = [9999] * n

dist[s] = 0

pq = [(0, s)]

while pq:

    cost, node = heapq.heappop(pq)

    for v, w in graph[node]:

        if dist[node] + w < dist[v]:

            dist[v] = dist[node] + w

            heapq.heappush(pq, (dist[v], v))

print(dist[d])