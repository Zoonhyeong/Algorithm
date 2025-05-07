# 2170 선 긋기
import sys

input = sys.stdin.readline

N = int(input())

line = []
for _ in range(N):
    x, y = map(int, input().split())
    line.append([x, y])

line.sort()
length = 0

first = line[0][0]
second = line[0][1]

if N == 1:
    print(line[0][1] - line[0][0])
    
else:
    for i in range(1, N):

        if i == N-1:
            if second <= line[i][0]:
                length += second - first
                length += line[i][1] - line[i][0]
            else:
                if line[i][1] <= second:
                    length += second - first
                else:
                    second = line[i][1]
                    length += second - first
        else:
            if second <= line[i][0]:
                length += second - first
                first = line[i][0]
                second = line[i][1]
            else:
                if second < line[i][1]:
                    second = line[i][1]

    print(length)