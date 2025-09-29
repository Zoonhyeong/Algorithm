# 9657 돌 게임 3

N = int(input())

dp = ['A'] * 1001

dp[1] = 'SK'
dp[2] = 'CY'
dp[3] = 'SK'
dp[4] = 'SK'
dp[5] = 'SK'
dp[6] = 'SK'
dp[7] = 'CY'

for i in range(8, N+1):
    if dp[i-1] == 'CY' or dp[i-3] == 'CY' or dp[i-4] == 'CY':
        dp[i] = 'SK'
    else:
        dp[i] = 'CY'

print(dp[N])