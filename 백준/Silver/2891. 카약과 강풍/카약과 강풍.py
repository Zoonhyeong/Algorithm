# 2891 카약과 강풍

N, S, R = map(int, input().split())

# 카약 손상된 팀
S_num = list(map(int, input().split()))
# 스페어가 있는 팀
R_num = list(map(int, input().split()))

# 손상 땜빵 가능 팀
T_num = set()

for i in range(len(R_num)):
    for j in range(len(S_num)):
        if R_num[i] == S_num[j]:
            T_num.add(R_num[i])

S_num = set(S_num) - T_num
R_num = set(R_num) - T_num

result = 0
for i in S_num:
    if i - 1 in R_num:
        R_num.remove(i - 1)
    elif i + 1 in R_num:
        R_num.remove(i + 1)
    else:
        result += 1

    """
    if i == 0:
        if i+1 in R_num:
            R_num.remove(i+1)
            continue
        else:
            result += 1
    elif i == N-1:
        if i-1 in R_num:
            R_num.remove(i-1)
            continue
        else:
            result += 1
    else:
        if i+1 in R_num:
            R_num.remove(i+1)
            continue
        elif i-1 in R_num:
            R_num.remove(i-1)
            continue
        else:
            result += 1"""

print(result)