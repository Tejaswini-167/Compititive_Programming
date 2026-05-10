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

# BFS

visited = [False] * n

queue = deque([start])

visited[start] = True

print("BFS:", end=" ")

while queue:

    node = queue.popleft()

    print(node, end=" ")

    for i in graph[node]:

        if not visited[i]:

            visited[i] = True

            queue.append(i)

# DFS

visited = [False] * n

def dfs(node):

    visited[node] = True

    print(node, end=" ")

    for i in graph[node]:

        if not visited[i]:
            dfs(i)

print("\nDFS:", end=" ")

dfs(start)