n = int(input())
table = set()

for i in range(n):
    table.add(input())

q = int(input())

for i in range(q):
    s = input()

    if s in table:
        print("Found")
    else:
        print("Not Found")