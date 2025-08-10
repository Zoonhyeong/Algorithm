# 14503 로봇 청소기
import sys
sys.setrecursionlimit(10**9)

def robot(x, y, d):
    result = 0
    while True:

        # 1번
        if place[x][y] == 0:
            place[x][y] = 2
            result += 1
        
        # 3번
        for i in range(4):
            d = (d - 1) % 4 # 방향 계산
            nx, ny = x + dx[d], y + dy[d]
            if 0 <= nx < N and 0 <= ny < M and place[nx][ny] == 0:
                x, y = nx,ny
                break # 이동했으니까 이제 for문을 더 돌 필요가 없음

        # 2번
        else:
            x, y = x + dx[d] * (-1), y + dy[d] * (-1)
            if 0 <= nx < N and 0 <= ny < M and place[x][y] == 1 or not 0 <= nx < N and 0 <= ny < M:
                print(result)
                return

N, M = map(int, input().split())

r, c, d = map(int, input().split())

# d : 0 - 북 / 1 - 동 / 2 - 남 / 3 - 서
place = []

for _ in range(N):
    temp = list(map(int, input().split()))
    place.append(temp)

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

robot(r, c, d)