n = int(input())

arr = list(map(int, input().split()))
x, k = map(int, input().split())

for i in range(n):

    if arr[i] == x:

        if i < k:
            print("Valid Access")
        else:
            print("Late Access")
        break
else:
    print("Access ID Not Found")