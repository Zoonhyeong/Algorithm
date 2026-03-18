# 4796 캠핑
i = 1
while True:
    L, P, V = map(int, input().split())
    if L == 0 and P == 0 and V == 0:
        break
    quotient = V // P
    remainder = V % P
    if L < remainder:
        remainder = L
    print(f'Case {i}: {quotient * L + remainder}')
    i += 1