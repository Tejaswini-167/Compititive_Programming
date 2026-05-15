# LAB 2.1 - Sum of Large Numbers Modulo

# Problem Statement:
# Given an array of integers and a modulo value m, calculate
# the sum of all array elements modulo m.


n = int(input())
m = int(input())

total = 0
for i in range(n):
    num = int(input())
    total = (total + num) % m

print(total)



n, m = map(int, input().split())
arr = list(map(int, input().split()))
# Compute sum modulo
total = 0
for num in arr:
 total = (total + num) % m
print(total)
