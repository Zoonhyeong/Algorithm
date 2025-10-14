# 16435 스네이크버드

N, L = map(int, input().split())

fruit = list(map(int, input().split()))

fruit.sort()

for i in range(N):
    if fruit[i] <= L:
        L += 1

print(L)