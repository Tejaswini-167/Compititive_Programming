# Lab 18.1 — Adjacency Matrix and Adjacency List
# PS Description

# This program represents a graph using adjacency matrix and adjacency list


n, e = map(int, input().split())

matrix = [[0]*n for i in range(n)]

graph = [[] for i in range(n)]

for i in range(e):

    u, v = map(int, input().split())

    matrix[u][v] = 1
    matrix[v][u] = 1

    graph[u].append(v)
    graph[v].append(u)

print("Adjacency Matrix")

for row in matrix:
    print(*row)

print("Adjacency List")

for i in range(n):
    print(i, "->", *graph[i])