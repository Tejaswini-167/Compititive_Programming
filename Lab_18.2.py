# Lab 18.2 — Connection Exists Between Users
# PS Description

# This program checks whether a connection/path exists between two users in a network using BFS


from collections import deque

n, e = map(int, input().split())

graph = [[] for i in range(n)]

for i in range(e):

    u, v = map(int, input().split())

    graph[u].append(v)
    graph[v].append(u)

s, d = map(int, input().split())

q = deque([s])

visited = [False] * n

visited[s] = True

while q:

    node = q.popleft()

    if node == d:
        print("Connection Exists")
        break

    for x in graph[node]:

        if not visited[x]:

            visited[x] = True

            q.append(x)

else:
    print("No Connection")