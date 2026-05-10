# Lab 24.2 — Simplest Code
# PS Description

# This program prints all squares reachable by a rook from a starting position on a chessboard.

n = int(input())

r, c = map(int, input().split())

print("Reachable Squares")

for i in range(n):

    if i != c:
        print(r, i)

for i in range(n):

    if i != r:
        print(i, c)