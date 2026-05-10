# Lab 24.1 — Simplest Code
# PS Description

# This program finds the minimum number of rook moves required to reach a target position on a chessboard.


n = int(input())

sr, sc = map(int, input().split())

tr, tc = map(int, input().split())

if sr == tr or sc == tc:
    print(1)

else:
    print(2)