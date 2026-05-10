files = set()
n = int(input())
for i in range(n):

    a = input().split()

    if a[0] == "CREATE":
        files.add(a[2])
        print("File Created")

    elif a[0] == "DELETE":

        if a[1] in files:
            files.remove(a[1])
            print("File Deleted")
        else:
            print("File Not Found")
    else:
        if a[1] in files:
            print("File Exists")
        else:
            print("File Not Found")