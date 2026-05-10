# Lab 14.1 — Brute Force String Matching
# PS Description

# This program checks whether a pattern string exists inside a text string using brute-force string matching.

# Input Format
# text
# pattern

# Example:

# ABABABC
# ABABC
# Output Format
# Pattern Found

# or

# Pattern Not Found

# Example:

# Pattern Found
# Simplest Code

text = input()

pattern = input()

if pattern in text:
    print("Pattern Found")

else:
    print("Pattern Not Found")