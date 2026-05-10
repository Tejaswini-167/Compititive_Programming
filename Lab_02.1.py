# LAB 2.1 - Sum of Large Numbers Modulo

# Problem Statement:
# Given an array of integers and a modulo value m, calculate
# the sum of all array elements modulo m.

# Important:
# Direct summation may cause overflow for very large numbers.
# So, modulo should be applied during the calculation itself.

# Task:
# - Accept n and m as input
# - Accept n integers in an array
# - Calculate the sum using modular addition
# - Print the final result as sum % m


# LAB 2.1 - Sum of Large Numbers Modulo

# n = int(input("Enter the number of items: "))
# m = int(input("Enter the modulo value: "))

# total = 0

# for i in range(n):
#     num = int(input("Enter value: "))
#     total = (total + num)
#     modulo = total % m

# print("Modulo =", modulo)



n = int(input())
m = int(input())

total = 0

for i in range(n):
    num = int(input())
    total = (total + num) % m

print(total)