# Lab 15.2 — Find Pattern Occurrences using KMP
# PS Description

# This program finds all starting positions where a pattern appears inside a text using KMP string matching and the LPS array



text = input()
pattern = input()

found = False

for i in range(len(text) - len(pattern) + 1):

    if text.startswith(pattern, i):
        print(i)
        found = True

if not found:
    print("Pattern Not Found")