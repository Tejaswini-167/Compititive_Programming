# Lab 12.2 — Minimum Speed and Maximum Time
# PS Description

# This program stores car speeds, finds the minimum speed, and 
# calculates the maximum time required to cross a fixed distance using:

# Time = Distance / Speed





n = int(input())

speeds = list(map(int, input().split()))
d = int(input())

minimum = speeds[0]
for s in speeds:

    if s < minimum:
        minimum = s

time = d / minimum

print("Minimum Speed =", minimum)
print(f"Maximum Time = {time:.2f} hours")