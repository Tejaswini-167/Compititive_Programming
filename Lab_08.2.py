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
arr = []
for _ in range(n):
    time, bib = map(int, input().split())
    arr.append((time, bib))

sorted_arr = quick_sort(arr)
print(sorted_arr)

for i in sorted_arr[:10]:
    print(i[0], i[1])



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