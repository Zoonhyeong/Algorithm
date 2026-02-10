# 9465 스티커
# import sys
# input = sys.stdin.readline

T = int(input())

for _ in range(T):
    sticker = []
    n = int(input())
    first = list(map(int, input().split()))
    second = list(map(int, input().split()))
    sticker.append(first)
    sticker.append(second)

    dp = [[0]*2 for i in range(n+1)]
    if n == 1:
        dp[1][0] = sticker[0][0]
        dp[1][1] = sticker[1][0]
        print(max(dp[n][0], dp[n][1]))
    elif n == 2:
        dp[1][0] = sticker[0][0]
        dp[1][1] = sticker[1][0]
        dp[2][0] = dp[1][1] + sticker[0][1]
        dp[2][1] = dp[1][0] + sticker[1][1]
        print(max(dp[n][0], dp[n][1]))
    else:
        dp[1][0] = sticker[0][0]
        dp[1][1] = sticker[1][0]
        dp[2][0] = dp[1][1] + sticker[0][1]
        dp[2][1] = dp[1][0] + sticker[1][1]
        for i in range(3, n+1):
            dp[i][0] = max(dp[i-1][1], dp[i-2][1]) + sticker[0][i-1]
            dp[i][1] = max(dp[i-1][0], dp[i-2][0]) + sticker[1][i-1]
        print(max(dp[n][0], dp[n][1]))