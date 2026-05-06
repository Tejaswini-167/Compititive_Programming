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


a = int(input("Enter base value: "))
m = int(input("Enter power value: "))
p = int(input("Enter modulo value: "))

result = 1
a = a % p

while m > 0:

    if m % 2 == 1:
        result = (result * a) % p

    a = (a * a) % p
    m = m // 2

print("Final Modulo =", result)