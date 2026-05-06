# LAB 3.1 - Modular Power Sum

# Problem Statement:
# Given n pairs of integers (a, m) and a prime number p,
# compute:

#      (a^m) % p

# for all pairs and find their sum modulo p.




n, p = map(int, input().split())

total = 0

for i in range(n):

    a, m = map(int, input().split())

    result = 1
    a = a % p

    while m > 0:

        if m % 2 == 1:
            result = (result * a) % p

        a = (a * a) % p
        m = m // 2

    total = (total + result) % p

print(total)


# Sample Input:
# 3 1000
# 2 10
# 3 5
# 5 3

# Sample Output:
# 392