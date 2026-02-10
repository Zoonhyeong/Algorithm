# 1744 수 묶기
import sys
input = sys.stdin.readline

N = int(input())
numbers = []
for _ in range(N):
    numbers.append(int(input()))
numbers.sort()

plus = []
minus = []
result = 0

# 양수, 음수(0 포함)
for i in range(N):
    if numbers[i] <= 0:
        minus.append(numbers[i])
    elif numbers[i] > 0:
        plus.append(numbers[i])

if len(plus) % 2 == 0: # 양-짝
    for i in range(0, len(plus), 2):
        if plus[i]*plus[i+1] > plus[i]+plus[i+1]:
            result += plus[i]*plus[i+1]
        else:
            result += plus[i]+plus[i+1]
else: # 양-홀
    for i in range(1, len(plus), 2):
        if plus[i]*plus[i+1] > plus[i]+plus[i+1]:
            result += plus[i]*plus[i+1]
        else:
            result += plus[i]+plus[i+1]
    result += plus[0]

if len(minus) % 2 == 0: # 음-짝
    for i in range(0, len(minus), 2):
        result += minus[i]*minus[i+1]
else: # 음-홀
    for i in range(0, len(minus)-1, 2):
        result += minus[i]*minus[i+1]
    result += minus[-1]

print(result)