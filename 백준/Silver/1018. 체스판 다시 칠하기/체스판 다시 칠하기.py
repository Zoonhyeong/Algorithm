# 1018 체스판 다시 칠하기
import sys
input = sys.stdin.readline

B_original_chess = ['BWBWBWBW', 'WBWBWBWB'] * 4
W_original_chess = ['WBWBWBWB', 'BWBWBWBW'] * 4

# 체스판
chess = []
N, M = map(int, input().split())
minValue = N*M

for i in range(N):
    chess.append(input().rstrip())

for i in range(N-7):
    for j in range(M-7):
        temp = 0
        for k in range(i,i+8):
            slice_chess = chess[k][j:j+8]
            for x in range(8):
                if B_original_chess[k-i][x] != slice_chess[x]:
                    temp += 1
        minValue = min(minValue, temp)

for i in range(N-7):
    for j in range(M-7):
        temp = 0
        for k in range(i,i+8):
            slice_chess = chess[k][j:j+8]
            for x in range(8):
                if W_original_chess[k-i][x] != slice_chess[x]:
                    temp += 1
        minValue = min(minValue, temp)

print(minValue)