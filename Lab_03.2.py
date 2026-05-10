# LAB 3.2 - Modular Multiplication Checker

# Problem Statement:
# Given integers a, b, p and k:
#
# Find:
#      (a * b) % p
#
# Check whether the result is divisible by k.
#
# Input:
# a b p k
#
# Output:
# Print "Divisible" or "Not Divisible"



a, b, p, k = map(int, input().split())

mod_product = ((a % p) * (b % p)) % p

if mod_product % k == 0:
    print("Divisible")
else:
    print("Not Divisible")


# Sample Input:
# 100000 200000 1000000 4
#
# Sample Output:
# Divisible