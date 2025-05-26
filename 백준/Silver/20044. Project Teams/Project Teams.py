# 20044 Project Teams

import sys

input = sys.stdin.readline

n = int(input())

result = []

coding = list(map(int, input().split()))

coding.sort()

for i in range(n):
    temp = coding[i] + coding[2*n - 1 - i]
    result.append(temp)

print(min(result))