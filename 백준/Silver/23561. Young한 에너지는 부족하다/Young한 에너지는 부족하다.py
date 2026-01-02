# 23561 Young한 에너지는 부족하다
import sys
input =  sys.stdin.readline

N = int(input())

crew = list(map(int, input().split()))

crew.sort()

print(crew[N*2-1] - crew[N])