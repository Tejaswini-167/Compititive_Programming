# LAB 2.2 - Modular Exponentiation

# Problem Statement:
# Given three integers a, m, and p, calculate:

#       (a ^ m) % p

# Important:
# Directly calculating a^m can create a very large number.
# So, modular exponentiation is used to avoid overflow.

# Task:
# - Accept a, m, and p as input
# - Calculate (a^m) % p efficiently
# - Print the final result




a =int(input("enter a value: "))
m = int(input("enter power value: "))
p = int(input("enter mod value: "))

result = 1
a=a % p
while m > 0:
    if m % 2 == 1: #check it m i s odd
        result = (result * a) % p

    a = (a * a) % p
    m = m // 2

print(result)

