# Lab 20.1 — Preorder Tree Traversal
# PS Description

# This code is using Tree Traversal (Preorder Traversal) to print all files and directories in a file system structure.

# Think of it like this:

n = int(input())

tree = {}

for i in range(n):
    node, left, right = map(int, input().split())
    tree[node] = (left, right)

def preorder(node):
    if node == -1:
        return

    print(node, end=" ")

    preorder(tree[node][0])
    preorder(tree[node][1])

print("File System Traversal (Preorder)")
preorder(1)