# Lab 11.1 — Small PS

# In a retail billing system, multiple product prices are stored in an array/list. 
# The program should display all product prices and calculate the total price of all products.

n = int(input())

prices = list(map(int, input().split()))

total = 0

for p in prices:
    print(p, end=" ")
    total = total + p

print()
print("Total Price =", total)