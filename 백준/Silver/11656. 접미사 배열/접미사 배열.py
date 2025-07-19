# 11656 접미사 배열

myStr = input()

N = len(myStr)

myList = []

for i in range(N):
    myList.append(myStr[i:])

myList.sort()

for i in range(N):
    print(myList[i])