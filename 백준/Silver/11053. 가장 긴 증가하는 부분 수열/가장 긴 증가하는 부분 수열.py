# 11053 가장 긴 증가하는 부분 수열

N = int(input())

myList = list(map(int, input().split()))
length = [0] * (N+1)

for i in range(N):
    length[i] = 1
    for j in range(i):
        if myList[j] < myList[i]:
            length[i] = max(length[j]+1, length[i])

print(max(length))