# 11478 서로 다른 부분 문자열의 개수

myStr = input()
myDict = {}

for i in range(1, len(myStr) + 1):
    for j in range(len(myStr)):
        tempStr = myStr[j:j+i]
        myDict[tempStr] = 1

print(len(myDict.keys()))