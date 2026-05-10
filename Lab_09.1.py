n = int(input())

arr = list(map(int, input().split()))

x = int(input())

for i in range(n):

    if arr[i] == x:
        print(i)
        break

else:
    print("Not Found")



# Time Complexity of Linear Search
# Best Case  : O(1)
# Worst Case : O(n)
# Average Case : O(n)


# When data is small
# When array is unsorted
# Simple and easy to implement
# Useful when sorting is not required