# 1439 뒤집기

one = 0
zero = 0

S = list(input())

for i in range(len(S)):
    if i == len(S) - 1:
        break

    if S[i] == '1':
        if S[i+1] == '0':
            zero += 1
        else:
            continue
    else:
        if S[i+1] == '1':
            one += 1
        else:
            continue

if zero == 0 and one == 0:
    print(0)
elif zero == 0:
    print(one)
elif one == 0:
    print(zero)
else:
    print(max(one, zero))