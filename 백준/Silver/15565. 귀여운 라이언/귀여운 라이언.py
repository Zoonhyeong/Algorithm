# 15565 귀여운 라이언

import sys

N, K = map(int, input().split())

dolls = list(map(int, input().split()))

answer = 10000000000

lion = [] # 라이언 위치
for i in range(len(dolls)):
    if dolls[i] == 1:
        lion.append(i)

# 윈도우의 크기 = end - start = 라이언 인형 개수
start = 0
end = K - 1

if len(lion) < K:
    print(-1)
    exit(0)

while True:
    doll = lion[end] - lion[start] + 1
    answer = min(answer, doll)
    if end == len(lion) - 1:
        break
    start += 1
    end += 1

print(answer)