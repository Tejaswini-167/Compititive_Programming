def quick_sort(arr):

    if len(arr) <= 1:
        return arr

    pivot = arr[0]

    left = []
    right = []

    for i in arr[1:]:

        if i < pivot:
            left.append(i)
        else:
            right.append(i)

    return quick_sort(left) + [pivot] + quick_sort(right)


n = int(input())
arr = list(map(int, input().split()))
sorted_arr = quick_sort(arr)

for i in sorted_arr:
    print(i, end=" ")



# Merge Sort
# Time Complexity:
# O(n log n)

# Divides data into smaller parts
# Sorting is very efficient
# Performance remains consistent even for large input sizes
# Faster than simple sorting methods like bubble sort or selection sort

# Quick Sort
# Time Complexity:
# Best/Average : O(n log n)
# Worst : O(n²)

# Very fast in practical applications
# Uses divide-and-conquer technique
# Requires less memory compared to merge sort
# Average performance is very efficient for large data