n = int(input())
books = {}

for i in range(n):

    title, bid = input().split()
    books[title] = int(bid)

q = int(input())

for i in range(q):
    s = input()

    if s in books:
        print(books[s])
    else:
        print("Book Not Found")