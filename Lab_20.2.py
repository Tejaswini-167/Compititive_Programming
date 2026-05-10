# Lab 20.2 — Preorder, Inorder, Postorder
# PS Description

# This program stores a binary tree and prints three traversals:

# Preorder  = Root Left Right
# Inorder   = Left Root Right
# Postorder = Left Right Root

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

def inorder(node):
    if node == -1:
        return
    inorder(tree[node][0])
    print(node, end=" ")
    inorder(tree[node][1])

def postorder(node):
    if node == -1:
        return
    postorder(tree[node][0])
    postorder(tree[node][1])
    print(node, end=" ")

print("Preorder Traversal")
preorder(1)

print("\nInorder Traversal")
inorder(1)

print("\nPostorder Traversal")
postorder(1)