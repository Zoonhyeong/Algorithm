# 10610 30

N = list(input())
N.sort(reverse=True)

temp = 0

if N[-1] == '0':
    for i in range(len(N)):
        temp += int(N[i])
    if temp % 3 == 0:
        print("".join(N))
    else:
        print(-1)
else:
    print(-1)