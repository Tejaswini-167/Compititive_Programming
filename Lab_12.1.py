# Lab 12.1 — Find Minimum Element
# PS Description

# This program stores numbers in an array/list and finds the minimum element using simple traversal without sorting.

# Input Format
# N
# array elements


n = int(input())

arr = list(map(int, input().split()))

minimum = arr[0]

for x in arr:

    if x < minimum:
        minimum = x

print(minimum)