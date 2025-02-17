# 10164 격자상의 경로
from itertools import combinations

def combination(a, b, c):
    min_num = 0
    result1 = 1
    result2 = 1

    if b > c :
        min_num = c
    else :
        min_num = b
    
    for i in range(min_num):
        result1 *= (a - i)
    for i in range(min_num):
        result2 *= (min_num - i)

    return result1 // result2

N, M, K = map(int, input().split())

if K == 0:
    print(combination(N+M-2, N-1, M-1))
else:
    row1 = K // M
    column1 = K % M - 1
    rst1 = combination(row1+column1, row1, column1)

    row2 = N - 1 - row1
    column2 = M - 1 - column1
    rst2 = combination(row2+column2, row2, column2)

    print(rst1 * rst2)