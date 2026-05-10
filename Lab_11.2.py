# Lab 11.2 — Total Cost Using Prices and Quantities
# PS Description

# This program stores product prices and quantities, then calculates the total bill
#  by multiplying each price with its quantity and adding all costs.

# Input Format
# N
# prices
# quantities

# Example:
# 4
# 100 50 20 10
# 2 5 3 4

# Output Format

# 550
# Simplest Code
n = int(input())

prices = list(map(int, input().split()))
qty = list(map(int, input().split()))

total = 0

for i in range(n):
    total = total + prices[i] * qty[i]

print(total)