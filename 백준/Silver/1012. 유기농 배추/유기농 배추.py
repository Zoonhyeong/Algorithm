# 1012 유기농 배추
import sys
from collections import deque
input = sys.stdin.readline

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

# a행 b열
def bfs(garden, a, b, M, N):
    queue = deque()
    count = 0
    if garden[a][b] == 0:
        return count
    else:
        queue.append((a, b))
        count = 1
        garden[a][b] = 0
        while queue:
            x, y = queue.popleft()
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if nx < 0 or nx >= N or ny < 0 or ny >= M:
                    continue
                if garden[nx][ny] == 1:
                    garden[nx][ny] = 0
                    queue.append((nx, ny))
        return count

# T : 테스트 수
T = int(input())

for _ in range(T):
    M, N, K = map(int, input().split())
    garden = [[0 for _ in range(M)] for _ in range(N)]
    result = 0

    # M : 가로 / N : 세로 / K : 배추 위치 수
    for _ in range(K):
        x, y = map(int, input().split())
        garden[y][x] = 1
    
    for i in range(N):
        for j in range(M):
            result += bfs(garden, i, j, M, N)

    print(result)