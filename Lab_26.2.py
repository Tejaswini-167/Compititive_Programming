# Lab 26.2 — Simplest Code
# PS Description

# This program checks whether two users belong to the same connected group using DSU.

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

        a = int(op[1])
        b = int(op[2])

        x = a
        y = b

        while parent[x] != x:
            x = parent[x]

        while parent[y] != y:
            y = parent[y]

        if x == y:
            print("Connected")

        else:
            print("Not Connected")