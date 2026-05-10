n = int(input())
arr = list(map(int,input().split()))
checksum = int(input())

ans = 0

for i in arr:
    ans = ans ^ i
    
if checksum == ans:
    print("OK")
else:
    print("ANOMOLY")