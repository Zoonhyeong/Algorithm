# 1912 연속합
import sys
input = sys.stdin.readline

N = int(input())
numList = list(map(int, input().split()))

maxResult = -1001
temp = 0
i = 0

while i < N:
    # 양수면 쭉쭉
    if numList[i] >= 0:
        temp += numList[i]
        maxResult = max(temp, maxResult)
        i += 1
    else:
        if temp >= abs(numList[i]):
            temp += numList[i]
            maxResult = max(temp, maxResult)
            i += 1
        else:
            temp += numList[i]
            maxResult = max(temp, maxResult)
            temp = 0
            i += 1

print(maxResult)