# 30804 과일 탕후루
import sys
input = sys.stdin.readline

N = int(input())

fruit = list(map(int, input().split()))

visited = {}

maxLen = 0
leftPoint = 0
rightPoint = 0

while rightPoint < N:
    nowTang = fruit[rightPoint]

    if nowTang in visited:
        visited[nowTang] += 1 # 딕셔너리에 있으면 nowTang값을 하나 추가
    else:
        visited[nowTang] = 1 # 딕셔너리에 없으면 하나 생성

    while len(visited) > 2: # 딕셔너리 크기가 2 이상이면 -> key : value 가 두개 이상이면 이라는 뜻
        removeTang = fruit[leftPoint]

        visited[removeTang] -= 1

        if visited[removeTang] == 0: # 없으면 키 자체를 삭제
            del visited[removeTang]

        leftPoint += 1
    maxLen = max(maxLen, rightPoint - leftPoint + 1)
    rightPoint += 1

print(maxLen)