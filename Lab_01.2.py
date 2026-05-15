# LAB 1.2 - Final Order Cost with Multiple Discounts

# Problem Statement:
# An online store provides item-level and order-level
# discounts on purchases.

# Item-Level Discount:
# - Each item may have its own percentage discount.
# - Discount is applied individually to every item.

# Order-Level Discount:
# - After calculating subtotal:
#     * If subtotal > 500  -> 10% discount
#     * If subtotal > 1000 -> 150 fixed discount


n = int(input("Enter number of items: "))

subtotal = 0

for i in range(n):
    price, discount_percent = map(int, input().split())
    item_cost = price - (price * discount_percent / 100)
    subtotal += item_cost

percentage_discount = 0
fixed_discount = 0

if subtotal > 500:
    percentage_discount = subtotal * 0.10

if subtotal > 1000:
    fixed_discount = 150

discount = max(percentage_discount, fixed_discount)
final_cost = subtotal - discount

print(int(final_cost))
