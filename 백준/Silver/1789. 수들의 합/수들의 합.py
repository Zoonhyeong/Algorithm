# 1789 수들의 합
S = int(input())
temp = 1
i = 1
while temp <= S:
    temp = i * (i+1) // 2
    i += 1

print(i-2)