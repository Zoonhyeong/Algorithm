# 16564 히오스 프로그래머
import sys

input = sys.stdin.readline

N, K = map(int, input().split())

levels = []

for i in range(N):
    levels.append(int(input()))

levels.sort()

# 범위 지정
start = levels[0]
end = levels[-1] + K

def get_diff(mid):
    diff = 0
    for level in levels:
        if level < mid:
            diff += mid - level
        else:
            break
    return diff

# 이진 탐색 실행
while start <= end:
    mid = (start + end) // 2
    diff = get_diff(mid)
    if diff <= K:
        start = mid+1
    else:
        end = mid - 1

# 최대로 가능한 레벨 출력
print(end)