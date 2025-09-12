# 21758 꿀 따기

N = int(input())
honey_pot = list(map(int, input().split()))

# result 1
result1 = 0
for i in range(1, N-1):
    temp1 = sum(honey_pot[1:i])
    temp2 = sum(honey_pot[i+1:]) * 2
    result1 = max(result1, temp1+temp2)

# result 2
result2 = 0
for i in range(1, N-1):
    temp1 = sum(honey_pot[:i]) * 2
    temp2 = sum(honey_pot[i+1:-1])
    result2 = max(result2, temp1+temp2)

# result 3
temp3 = honey_pot.index(max(honey_pot[1:-1]))
result3 = sum(honey_pot[1:temp3+1]) + sum(honey_pot[temp3:-1])

print(max(result1, result2, result3))