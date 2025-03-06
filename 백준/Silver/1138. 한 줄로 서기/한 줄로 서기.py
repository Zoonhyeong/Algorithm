# 1138 한 줄로 서기

N = int(input())

info = list(map(int, input().split()))
line = [0] * N

for i in range(N):
    temp = 0
    for j in range(N):
        if info[i] == temp:
            now = j
            break
        if line[j] == 0:
            temp += 1
    # line[temp]가 0이면 현재 값 추가 아니면 다음 자리 확인
    for k in range(N):
        if line[now + k] == 0:
            line[now + k] = i + 1
            break
print(*line)