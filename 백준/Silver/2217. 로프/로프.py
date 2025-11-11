# 2217 로프
# k개 로프, 중량 w -> 각각엔 w/k
import sys

input = sys.stdin.readline

N = int(input())

rope = []
for _ in range(N):
    rope.append(int(input()))

rope.sort()

max_weight = 0

for i in range(N):
    weight = rope[i] * (N-i)
    if weight > max_weight:
        max_weight = weight

print(max_weight)