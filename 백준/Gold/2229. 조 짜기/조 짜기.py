# 2229 조 짜기
import sys

input = sys.stdin.readline

N = int(input())

student = list(map(int, input().split()))

if N == 1:
    print(0)
else:
    dp = [0] * (N+1)
    
    for i in range(1, N+1):
        max_v, min_v = 0, 10001

        for j in range(i, 0, -1):
            max_v = max(max_v, student[j-1])
            min_v = min(min_v, student[j-1])
            dp[i] = max(dp[i], max_v - min_v + dp[j-1])

    print(dp[N])