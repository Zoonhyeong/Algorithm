# 16121 정열적인 정렬
import sys
input = sys.stdin.readline

N = int(input())
myList = list(map(int, input().split()))

myList.sort()

print(*myList)