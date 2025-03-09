# 23304 아카라카

def AKARAKA(s):
    global result

    if len(s) == 1:
        result = "AKARAKA"
        return
    else:
        if s != s[::-1]:
            return
        else:
            N = len(s) // 2
            AKARAKA(s[:N])
            AKARAKA(s[-N:])

S = input()

result = "IPSELENTI"
AKARAKA(S)

print(result)