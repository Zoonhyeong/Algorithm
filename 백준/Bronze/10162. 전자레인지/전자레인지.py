# 10162 전자레인지
import sys
input = sys.stdin.readline

T = int(input())
A = 0
B = 0
C = 0

A = T // 300
T = T % 300
    
B = T // 60
T = T % 60

C = T // 10
T = T % 10

if T == 0:
    print(A, B, C)
else:
    print(-1)