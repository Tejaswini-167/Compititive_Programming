



from collections import defaultdict

tree=defaultdict(list)
files=set()

n = int(input("enter no of entries"))

for i in range(n):
    d,f=input().split()
    tree[d].append(f)
    files.add(f)

s =input("enter the file to search")

print("file system structure")
for i in tree:
    print(i,"->",*tree[i])

if s in files:
    print(f"{s} found")
