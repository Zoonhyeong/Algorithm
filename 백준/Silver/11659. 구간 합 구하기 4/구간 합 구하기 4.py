# 11659 구간 합 구하기 4
import sys
input = sys.stdin.readline

N, M = map(int, input().split())

numList = list(map(int, input().split()))

tempList = []
for _ in range(M):
    a, b = map(int, input().split())
    tempList.append([a, b])

prefixSum = [0] * N

# numList : 5 4 3 2 1
# N : 5
# prefixSum : 5 9 12 14 15

for i in range(N): # 0 1 2 3 4
    if i == 0:
        prefixSum[i] = numList[i]
    else:
        prefixSum[i] = prefixSum[i-1] + numList[i]

for i in range(M):
    a, b = tempList[i]
    if a == 1:
        print(prefixSum[b-1])
    else:
        print(prefixSum[b-1] - prefixSum[a-2])