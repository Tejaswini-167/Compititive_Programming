# Lab 14.1 — Brute Force String Matching
# PS Description

# This program checks whether a pattern string exists inside a text string using brute-force string matching.

# Input Format
# text
# pattern



text = input()

pattern = input()

if pattern in text:
    print("Pattern Found")

else:
    print("Pattern Not Found")