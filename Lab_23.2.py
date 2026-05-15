# Lab 23.2 — Discount + Coupon
# PS Description

# This program stores cart items, applies item discounts, calculates total price, and 
# applies a coupon if the total is greater than or equal to the threshold.


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

coupon, threshold = map(int, input().split())

for i in items:
    print(i, items[i])
    total += items[i]

print("Price After Discount =", total)

if total >= threshold:
    total -= coupon

print("Final Cart Price =", total)