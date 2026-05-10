# Simplified 17.2 (VERY SHORT)
# PS Description

# This program checks whether a path exists between two nodes in a graph.

# Simple Code
from collections import deque

n, e = map(int, input().split())

graph = [[] for i in range(n)]

for i in range(e):

    u, v = map(int, input().split())

    graph[u].append(v)
    graph[v].append(u)

s, d = map(int, input().split())

queue = deque([s])

visited = [False] * n

visited[s] = True

found = False

while queue:

    node = queue.popleft()

    if node == d:
        found = True
        break

    for i in graph[node]:

        if not visited[i]:

            visited[i] = True

            queue.append(i)

if found:
    print("Path Exists")

else:
    print("No Path Exists")