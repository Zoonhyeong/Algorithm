# 2143 두 배열의 합
import sys
from collections import Counter

input = sys.stdin.readline

T = int(input())
N = int(input())
N_list = list(map(int, input().split()))
M = int(input())
M_list = list(map(int, input().split()))

prefix_N = []
prefix_M = []

result = 0

for i in range(N):
    for j in range(i+1, N+1):
        prefix_N.append(sum(N_list[i:j]))

for i in range(M):
    for j in range(i+1, M+1):
        prefix_M.append(sum(M_list[i:j]))

prefix_N.sort()
prefix_M.sort()

counter_N = Counter(prefix_N)
counter_M = Counter(prefix_M)

for key in counter_N:
    target = T - key
    result += counter_N[key] * counter_M[target]

print(result)