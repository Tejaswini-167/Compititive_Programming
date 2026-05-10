# Lab 12.2 — Minimum Speed and Maximum Time
# PS Description

# This program stores car speeds, finds the minimum speed, and 
# calculates the maximum time required to cross a fixed distance using:

# Time = Distance / Speed

# Input Format
# N
# car speeds
# distance

# Example:

# 5
# 60 45 80 50 40
# 10
# Output Format
# Minimum Speed
# Maximum Time

# Example:

# Minimum Speed = 40
# Maximum Time = 0.25 hours
# Simplest Code

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