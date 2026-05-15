# Lab 23.1 — Discount on Items
# PS Description

# This program stores cart items with prices, applies discounts to matching items, and prints the total price after discount.



n = int(input())
items = {}
total = 0
for i in range(n):

    name, price = input().split()
    items[name] = int(price)

d = int(input())
for i in range(d):
    name, dis = input().split()
    
    if name in items:
        items[name] -= items[name] * int(dis) // 100

for i in items:

    print(i, items[i])
    total += items[i]

print("Total Price =", total)