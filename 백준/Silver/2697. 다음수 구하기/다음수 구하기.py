# 2697 다음수 구하기

T = int(input())

def myfunc(numList):
    first = numList[0]
    minNums = []
    for i in range(1, len(numList)):
        if first < numList[i]:
            minNums.append(numList[i])
    minNum = min(minNums)
    numList.remove(minNum)
    numList.sort()
    numList.insert(0, minNum)

    return numList

for _ in range(T):
    num = input()
    if len(num) == 2:
        if int(num[0]) >= int(num[1]):
            print("BIGEST")
        else:
            print(num[1]+num[0])
    else:
        for i in range(len(num)-1, 0, -1):
            if num[i] <= num[i-1]:
                continue
            elif num[i] > num[i-1]:
                j = i - 1
                temp1 = num[:j]
                temp2 = "".join(myfunc(list(num[j:])))
                result = temp1 + temp2
                print(result)
                break
        else:
            print("BIGGEST")