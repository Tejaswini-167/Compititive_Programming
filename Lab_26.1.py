# Lab 26.1 — Simplest Code
# PS Description

# This program manages groups using Disjoint Set Union (DSU) and performs union and find operations.

n = int(input())

m = int(input())

parent = list(range(n + 1))

for i in range(m):

    op = input().split()

    if op[0] == "union":

        a = int(op[1])
        b = int(op[2])

        parent[b] = a

    else:

        x = int(op[1])

        while parent[x] != x:
            x = parent[x]

        print(x)