# 2467 용액
import sys

input = sys.stdin.readline

N = int(input())

liquid = list(map(int, input().split()))

start = 0
end = len(liquid) - 1

min_value = sys.maxsize
answer = (liquid[start], liquid[end])  # 결과 저장용

while start < end :
    sum_value = liquid[start] + liquid[end]
    if abs(sum_value) < min_value:
        min_value = abs(sum_value)
        answer = (liquid[start], liquid[end])

    if sum_value == 0:
        print(answer[0], answer[1])
        exit()
    elif sum_value < 0:
        start += 1
    else:
        end -= 1

print(answer[0], answer[1])