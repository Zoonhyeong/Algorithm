# 1991 트리 순회

tree = {}

N = int(input())

for _ in range(N):
    root, left, right = map(str, input().split())
    tree[root] = [left, right]

def preorder(root):
    if root != '.':
        print(root, end='')  # root
        preorder(tree[root][0])  # left
        preorder(tree[root][1])  # right

def inorder(root):
    if root != '.':
        inorder(tree[root][0])  # left
        print(root, end='')  # root
        inorder(tree[root][1])  # right

def postorder(root):
    if root != '.':
        postorder(tree[root][0])  # left
        postorder(tree[root][1])  # right
        print(root, end='')  # root

preorder('A')
print()
inorder('A')
print()
postorder('A')