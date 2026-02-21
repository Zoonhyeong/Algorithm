# 1049 기타줄
import sys
input = sys.stdin.readline

N, M = map(int, input().split())

brands = []

for i in range(M):
    brand, one = map(int, input().split())
    brands.append([brand, one])

# 패키지로 계산
brands.sort(key=lambda x : x[0])
package = brands[0][0]

brands.sort(key=lambda x : x[1])
one = brands[0][1]

if 6 * one <= package:
    print(one*N)
else:
    temp = N // 6 * package
    if one * (N % 6) >= package:
        temp += package
    else:
        temp += one * (N % 6)
    print(temp)