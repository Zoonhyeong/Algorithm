from math import comb

N, M, K = map(int, input().split())

if K == 0:
    print(comb(N + M - 2, N - 1))
else:
    # K를 0-based index로 변경
    K -= 1
    
    row1 = K // M
    column1 = K % M

    rst1 = comb(row1 + column1, row1)

    row2 = N - 1 - row1
    column2 = M - 1 - column1
    rst2 = comb(row2 + column2, row2)

    print(rst1 * rst2)