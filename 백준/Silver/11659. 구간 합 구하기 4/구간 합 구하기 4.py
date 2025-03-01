# 11659 구간 합 구하기 4
import sys
input = sys.stdin.readline

N, M = map(int, input().split())

numList = list(map(int, input().split()))


prefixSum = [0] * N

# numList : 5 4 3 2 1
# N : 5
# prefixSum : 5 9 12 14 15

for i in range(N): # 0 1 2 3 4
    if i == 0:
        prefixSum[i] = numList[i]
    else:
        prefixSum[i] = prefixSum[i-1] + numList[i]

result = []
for i in range(M):
    a, b = map(int, input().split())
    if a == 1:
        result.append(prefixSum[b-1])
    else:
        result.append(prefixSum[b-1] - prefixSum[a-2])

for rst in result:
    print(rst)