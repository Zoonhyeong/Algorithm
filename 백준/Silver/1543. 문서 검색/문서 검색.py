# 1543 문서 검색

document = list(input())

target = list(input())

result = 0
T = len(document) - len(target)

i = 0

while i <= T:
    if document[i:i+len(target)] == target[:]:
        result += 1
        i = i + len(target)
    else:
        i += 1

print(result)