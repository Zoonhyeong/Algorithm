# 11054 가장 긴 바이토닉 부분수열
import sys
input = sys.stdin.readline

N = int(input())
myList = list(map(int, input().split()))
re_myList = list(reversed(myList))

dp_up = [1]*(N+1)
dp_down = [1]*(N+1)
temp_list = []
max_result = 0

for i in range(2, N+1):
    for j in range(i):
        if myList[i-1] > myList[j]:
            dp_up[i] = max(dp_up[i], dp_up[j+1] + 1)

for i in range(2, N+1):
    for j in range(i):
        if re_myList[i-1] > re_myList[j] :
            dp_down[i] = max(dp_down[i], dp_down[j+1] + 1)

dp_down = list(reversed(dp_down))
dp_down.insert(0, 1)
dp_down.pop(-1)

for i in range(1, N+1):
    max_result = max(max_result, dp_up[i] + dp_down[i] - 1)

print(max_result)