# Lab 13.2 — Minimum Time for Cars to Pass
# PS Description

# This program stores car lengths and speeds, calculates the time taken by each car using:

# Time = Length / Speed

# and prints the maximum time required for all cars to pass the checkpoint.



n = int(input())

lengths = list(map(int, input().split()))
speeds = list(map(int, input().split()))

max_time = 0

for i in range(n):

    time = lengths[i] / speeds[i]

    if time > max_time:
        max_time = time

print(int(max_time))