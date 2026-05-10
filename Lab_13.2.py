# Lab 13.2 — Minimum Time for Cars to Pass
# PS Description

# This program stores car lengths and speeds, calculates the time taken by each car using:

# Time = Length / Speed

# and prints the maximum time required for all cars to pass the checkpoint.

# Input Format
# N
# lengths
# speeds

# Example:

# 4
# 4 2 6 3
# 2 3 1 2
# Output Format
# maximum time

# Example:

# 6
# Simplest Code

n = int(input())

lengths = list(map(int, input().split()))
speeds = list(map(int, input().split()))

max_time = 0

for i in range(n):

    time = lengths[i] / speeds[i]

    if time > max_time:
        max_time = time

print(int(max_time))