# 2178 미로 탐색
from collections import deque

def bfs(maze, N, M):
    # 방문해야 할 노드를 저장하는 Queue
    need_visited = deque([])
    
    # 방문 O X
    visited = [[False]*M for i in range(N)]

    # 거리 계산
    distance = [[1]*M for i in range(N)]

    # Start
    visited[0][0] = True
    need_visited.append((0,0))

    # 방향(상하좌우 --> 인접리스트를 옆으로 눕힌다고 생각)
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]

    while need_visited: # 큐에 있는게 다 빠질 때까지
        x, y = need_visited.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            # 범위 넘어가면 GG
            if nx < 0 or ny < 0 or nx >= N or ny >= M:
                continue
            
            # 방문 안했고 이동 가능하면 GO
            if visited[nx][ny] == False and maze[nx][ny] == 1:
                need_visited.append((nx,ny))
                visited[nx][ny] = True
                distance[nx][ny] += distance[x][y]
            
            if visited[nx][ny] == True and nx == N-1 and ny == M-1:
                origin = distance[nx][ny]
                if distance[x][y] + 1 > origin:
                    distance[nx][ny] = origin
                else:
                    distance[nx][ny] = distance[x][y] + 1

    return distance[N-1][M-1]

N, M = map(int, input().split())
maze = []
for _ in range(N):
    maze.append(list(map(int, input())))

print(bfs(maze, N, M))