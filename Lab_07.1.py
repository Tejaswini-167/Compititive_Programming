# 7.1 Problem Statement: Store Finishing Times in an Array/List
# Problem Description
# You are conducting a race event and need to record the finishing times of participants.
# The user will enter N numerical finishing times, and your task is to store all the values
# correctly in a basic data structure such as an array (C/Java) or list (Python) and print them
# in the same order.

n = int(input())
arr = list(map(int,input().split()))

#print(arr)
for i in arr:
    print(i,end= " ")