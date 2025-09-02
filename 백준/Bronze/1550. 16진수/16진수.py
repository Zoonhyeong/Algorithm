# 1550 16진수

myStr = list(input())
result = 0

for i in range(len(myStr)-1, -1, -1):
    if myStr[i] == 'A':
        result += 16 ** (len(myStr)-1-i) * 10
    elif myStr[i] == 'B':
        result += 16 ** (len(myStr)-1-i) * 11
    elif myStr[i] == 'C':
        result += 16 ** (len(myStr)-1-i) * 12
    elif myStr[i] == 'D':
        result += 16 ** (len(myStr)-1-i) * 13
    elif myStr[i] == 'E':
        result += 16 ** (len(myStr)-1-i) * 14
    elif myStr[i] == 'F':
        result += 16 ** (len(myStr)-1-i) * 15
    else:
        result += 16 ** (len(myStr)-1-i) * int(myStr[i])
    
print(result)