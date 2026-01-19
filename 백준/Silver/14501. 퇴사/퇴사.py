# 14501 퇴사
import sys
input = sys.stdin.readline

N = int(input())
counsel = []
for i in range(N):
    counsel.append(list(map(int, input().split())))

def solve(i):
    if i >= N:
        return 0
    
    maxResult = 0
    if i + counsel[i][0] <= N:
        maxResult = solve(i+counsel[i][0]) + counsel[i][1]
    maxResult = max(maxResult, solve(i+1))
    return maxResult

print(solve(0))