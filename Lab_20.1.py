# Lab 20.1 — Preorder Tree Traversal
# PS Description

# This program stores a binary tree and prints all nodes using preorder traversal.

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