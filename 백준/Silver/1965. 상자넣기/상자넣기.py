# 1965 상자넣기
import sys

input = sys.stdin.readline

N = int(input())

Box = list(map(int, input().split()))

dp = [1] * N

for i in range(N):
    for j in range(i):
        if Box[i] > Box[j]:
            dp[i] = max(dp[i], dp[j]+1)

print(max(dp))