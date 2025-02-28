# 11441 누적 합
import sys

input = sys.stdin.readline

N = int(input())

numList = list(map(int, input().split()))

M = int(input())

tempList = []

for i in range(M):
    a, b = map(int, input().split())
    tempList.append([a, b])

# 누적 합 계산
prefix_sum = [0] * (N + 1)
for i in range(1, N + 1):
    prefix_sum[i] = prefix_sum[i - 1] + numList[i - 1]

result = []
for a, b in tempList:
    # 각 구간의 합을 효율적으로 계산
    result.append(prefix_sum[b] - prefix_sum[a - 1])

# 원하는 값 출력
for res in result:
    print(res)