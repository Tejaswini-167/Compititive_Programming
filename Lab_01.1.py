# LAB 1.1 - Tiered Discount Calculator

# Problem Statement:
# A shopping website offers discounts based on the total
# purchase amount.

# Discount Rules:
# 1. If amount < 1000       -> No discount
# 2. If amount >= 1000 and < 5000  -> 10% discount
# 3. If amount >= 5000 and < 10000 -> 20% discount
# 4. If amount >= 10000 -> 25% discount + 500 flat discount



amount = int(input("Enter total purchase amount: "))

if amount < 1000:
    final_amount = amount
elif amount < 5000:
    final_amount = amount - (amount * 0.10)
elif amount < 10000:
    final_amount = amount - (amount * 0.20)
else:
    final_amount = amount - (amount * 0.25) - 500

print("Final amount to be paid:", int(final_amount))