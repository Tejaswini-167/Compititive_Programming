# Lab 19.1 — Shortest Path Using Dijkstra
# PS Description

# This program finds the shortest distance from a source node to all other nodes using Dijkstra’s algorithm.


import heapq

n, e = map(int, input().split())

graph = [[] for i in range(n)]

for i in range(e):

    u, v, w = map(int, input().split())

    graph[u].append((v, w))
    graph[v].append((u, w))

src = int(input())

dist = [9999] * n

dist[src] = 0

pq = [(0, src)]

while pq:

    d, node = heapq.heappop(pq)

    for v, w in graph[node]:

        if dist[node] + w < dist[v]:

            dist[v] = dist[node] + w

            heapq.heappush(pq, (dist[v], v))

print(*dist)