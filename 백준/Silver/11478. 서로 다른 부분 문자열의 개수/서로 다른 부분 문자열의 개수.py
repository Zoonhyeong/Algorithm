# 11478 서로 다른 부분 문자열의 개수

myStr = input()
myDict = {}
mySet = set()

for i in range(1, len(myStr) + 1):
    for j in range(len(myStr)):
        tempStr = myStr[j:j+i]
        mySet.add(tempStr)

print(len(mySet))