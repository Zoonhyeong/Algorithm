# 11660 구간 합 구하기 5
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
square = [list(map(int, input().split())) for _ in range(N)]

# 2차원 누적 합 배열 생성
prefix_sum = [[0] * (N + 1) for _ in range(N + 1)]

for i in range(1, N + 1):
    for j in range(1, N + 1):
        # 현재 위치의 누적 합은 왼쪽, 위, 그리고 대각선 왼쪽 위를 이용하여 구함
        prefix_sum[i][j] = (square[i - 1][j - 1] + prefix_sum[i - 1][j] + prefix_sum[i][j - 1] - prefix_sum[i - 1][j - 1])

# 쿼리 처리
results = []
for _ in range(M):
    x1, y1, x2, y2 = map(int, input().split())
    
    # (x1, y1)부터 (x2, y2)까지의 구간 합 계산
    result = (prefix_sum[x2][y2] - prefix_sum[x1 - 1][y2] - prefix_sum[x2][y1 - 1] + prefix_sum[x1 - 1][y1 - 1])
    
    results.append(result)

for result in results:
    print(result)