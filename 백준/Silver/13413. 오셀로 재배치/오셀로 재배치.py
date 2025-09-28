# 13413 오셀로 재배치
import sys

input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N = int(input())
    initial = list(input())
    target = list(input())
    black = 0
    white = 0
    for i in range(N):
        if initial[i] == target[i]:
            continue
        else:
            if initial[i] == 'B':
                black += 1
            else:
                white += 1
    print(max(black, white))