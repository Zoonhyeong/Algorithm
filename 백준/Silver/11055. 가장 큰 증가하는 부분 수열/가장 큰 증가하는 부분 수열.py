# 11055 가장 큰 증가하는 부분 수열
import sys
input = sys.stdin.readline

N = int(input())
myList = list(map(int, input().split()))

dp = [0] * (N+1)

dp[1] = myList[0]

for i in range(2, N+1):
    for j in range(i):
        if myList[i-1] > myList[j-1]:
            dp[i] = max(dp[i], dp[j] + myList[i-1])
        else:
            dp[i] = max(dp[i], myList[i-1])

print(max(dp))