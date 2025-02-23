# 1927 최소 힙
import sys
import heapq

input = sys.stdin.readline
hip = []

N = int(input())

for _ in range(N):
    num = int(input())

    if num == 0:
        if len(hip):
            print(heapq.heappop(hip))
        else:
            print(0)
    else:
        heapq.heappush(hip, num)