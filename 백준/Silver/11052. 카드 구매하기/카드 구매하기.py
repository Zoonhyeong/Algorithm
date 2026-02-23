# 11052 카드 구매하기
import sys
input = sys.stdin.readline

N = int(input())
cards = list(map(int, input().split()))

dp = [0] * (N+1)

if N == 1:
    dp[1] = cards[0]
elif N == 2:
    dp[1] = cards[0]
    dp[2] = max(dp[1]*2, cards[1])
elif N == 3:
    dp[1] = cards[0]
    dp[2] = max(dp[1]*2, cards[1])
    dp[3] = max(dp[2]+dp[1], cards[2])
else:
    dp[1] = cards[0]
    dp[2] = max(dp[1]*2, cards[1])
    dp[3] = max(dp[2]+dp[1], cards[2])
    for i in range(4,N+1):
        temp_list = []
        for j in range(1, i//2+1):
            temp_list.append(dp[j]+dp[i-j])
        temp_list.append(cards[i-1])
        dp[i] = max(temp_list)

print(dp[N])