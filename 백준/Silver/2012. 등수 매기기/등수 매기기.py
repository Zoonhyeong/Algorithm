# 2012 등수 매기기
import sys

input = sys.stdin.readline

N = int(input())

result = 0
rank = []
temp_rank = []

for i in range(N):
    temp = int(input())
    temp_rank.append(temp)
temp_rank.sort()


for i in range(1, N+1):
    rank.append([i, temp_rank[i-1]])


for i in range(N):
    result += abs(rank[i][0] - rank[i][1])

print(result)