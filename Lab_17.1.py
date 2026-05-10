# Lab 17.1 — BFS and DFS Traversal
# PS Description

# This program stores a graph and performs BFS and DFS traversal starting from a given node.

# Input Format
# N E
# edges
# start node

# Example:

# 5 4
# 0 1
# 0 2
# 1 3
# 2 4
# 0
# Output Format
# BFS Traversal
# DFS Traversal

# Example:

# 0 1 2 3 4
# 0 1 3 2 4
# Simplest Code
from collections import deque

n, e = map(int, input().split())

graph = [[] for i in range(n)]

for i in range(e):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

start = int(input())

visited = [False] * n
q = deque([start])
visited[start] = True

print("BFS Traversal:", end=" ")

while q:
    node = q.popleft()
    print(node, end=" ")

    for x in graph[node]:
        if not visited[x]:
            visited[x] = True
            q.append(x)

visited = [False] * n
stack = [start]

print("\nDFS Traversal:", end=" ")

while stack:
    node = stack.pop()

    if not visited[node]:
        visited[node] = True
        print(node, end=" ")

        for x in reversed(graph[node]):
            if not visited[x]:
                stack.append(x)