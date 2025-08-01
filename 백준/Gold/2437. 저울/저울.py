# 2437 저울
import sys

input = sys.stdin.readline

N = int(input())

weight = list(map(int, input().split()))

weight.sort()

prior = [0, 0]
next = [0, 0]

for num in weight:
    next[0], next[1] = prior[0] + num, prior[1] + num
    if prior[1] + 1 >= next[0]:
        prior[1] = next[1]
    else:   
        print(prior[1] + 1)
        break
else:
    print(prior[1] + 1)