# 13975 파일 합치기 3
# 작은거 두개 합치고 리스트에 다시 박은 다음에 다시 작은거 두개 앞에서 가면 됨

import sys
import heapq

input = sys.stdin.readline

T = int(input())

for _ in range(T):
    temp = 0

    K = int(input())
    chapter = list(map(int, input().split()))

    # heapq.heapify(chapter)
    heap = []

    for i in range(K):
        heapq.heappush(heap, chapter[i])

    for i in range(K-1):
        a = heapq.heappop(heap)
        b = heapq.heappop(heap)
        temp += a+b
        heapq.heappush(heap, a+b)

    print(temp)