# 1202 보석 도둑
import sys
import heapq
input = sys.stdin.readline

N, K = map(int, input().split())

gems = []
bags = []
max_price = 0

for _ in range(N):
    M, V = map(int, input().split())
    gems.append([M,V])

for _ in range(K):
    C = int(input())
    bags.append(C)

gems.sort() # 보석 무게순으로 정렬
bags.sort() # 가방 무게순으로 정렬

temp_heapq = [] # 

for bag in bags:
    while gems and gems[0][0] <= bag: # 가방보다 작으면 보석을 임시 힙에다가 저장
        heapq.heappush(temp_heapq, -gems[0][1]) # 최대 힙을 구현해야하니까 음수를 붙임
        heapq.heappop(gems) # 보석 이미 임시힙에 박아놨으니까 원래 리스트에서 제거
    if temp_heapq:
        max_price += -heapq.heappop(temp_heapq)

print(max_price)