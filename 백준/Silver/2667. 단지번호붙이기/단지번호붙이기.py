# 2667 단지번호붙이기
import sys
from collections import deque
input = sys.stdin.readline

def bfs(maps, visited, i, j):
    queue = deque([(i,j)])

    distance = 1
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    visited[i][j] = True

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
        
            # 범위 넘어가면 GG
            if nx < 0 or ny < 0 or nx >= N or ny >= N:
                continue
            
            # 방문 안했고 이동 가능하면 GO
            if visited[nx][ny] == False and maps[nx][ny] == 1:
                queue.append((nx,ny))
                visited[nx][ny] = True
                distance += 1
        
    return distance

N = int(input())
maps = []
result = []
for i in range(N):
    maps.append(list(map(int, input().rstrip())))

visited = [[False]* (N+1) for _ in range(N)]
for i in range(N):
    for j in range(N):
        if visited[i][j] == False and maps[i][j] == 1:
            result.append(bfs(maps, visited, i, j))

result.sort()
print(len(result))
for i in range(len(result)):
    print(result[i])