# 1932 정수 삼각형
import sys
input = sys.stdin.readline

N = int(input())

myList = []

for i in range(N):
    myList.append((list((map(int, (input().split()))))))
myList = sorted(myList, key=len, reverse=True) # key를 길이로 해서 내림차순 정렬

for i in range(1, N):
    for j in range(N-i):
        myList[i][j] = max(myList[i-1][j], myList[i-1][j+1]) + myList[i][j]

print(*myList[N-1])