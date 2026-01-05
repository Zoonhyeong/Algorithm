from collections import deque

dx = [1,0,-1,0]
dy = [0,1,0,-1]

X, Y, N = map(int, input().split())

graph = [[0]*1000 for _ in range(1000)] # 절대값 때문에
for _ in range(N):
    A, B = map(int, input().split())
    graph[A][B] = -1

visited = [[False]*1000 for _ in range(1000)]

def bfs(x,y):
    q = deque([(x,y,0)])
    visited[x][y] = True
    
    while q:
        x, y, count = q.popleft()

        if x == X and y == Y:
            return count
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if -500 <= nx < 500 and -500 <= ny < 500:
                if not visited[nx][ny] and graph[nx][ny] != -1:
                    visited[nx][ny] = True
                    q.append([nx, ny, count+1])

print(bfs(0,0))