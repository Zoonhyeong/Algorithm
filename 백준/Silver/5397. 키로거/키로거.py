import sys
input = sys.stdin.readline

n = int(input())

for i in range(n):
    password = input().strip()
    left, right = [], []

    for j in password:
        if j == '<':
            if left:
                right.append(left.pop())
        elif j == '>':
            if right:
                left.append(right.pop())
        elif j == '-':
            if left:
                left.pop()
        else:
            left.append(j)

    # Do not sort, just reverse right and extend left
    result = left + right[::-1]

    print(''.join(result))