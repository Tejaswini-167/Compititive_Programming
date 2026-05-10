# Lab 15.1 — Build LPS Array
# PS Description

# This program constructs the LPS (Longest Proper Prefix which is also Suffix) array used in KMP string matching.


p = input()

lps = [0]

for i in range(1, len(p)):

    x = 0

    for j in range(i):

        if p[:j+1] == p[i-j:i+1]:
            x = j + 1

    lps.append(x)

print(*lps)