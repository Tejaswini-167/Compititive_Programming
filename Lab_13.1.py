# Lab 13.1 — Two Pointer Car Movement
# PS Description

# This program uses the two-pointer technique to process cars from both left and right sides alternately.

# Input Format
# N
# distances


n = int(input())

arr = list(map(int, input().split()))

left = 0
right = n - 1

while left <= right:

    if left == right:
        print(arr[left], end=" ")

    else:
        print(arr[left], arr[right], end=" ")

    left += 1
    right -= 1