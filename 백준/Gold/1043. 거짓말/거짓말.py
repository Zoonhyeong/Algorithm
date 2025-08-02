# 1043 거짓말
import sys

input = sys.stdin.readline

N, M = map(int, input().split())
know = set(map(int, input().split()[1:]))
party = []

for i in range(M):
    people = set(map(int, input().split()[1:]))
    party.append(people)

can = [True] * M

for _ in range(M):
    for i, people in enumerate(party):
        if people & know: # 파티에 참여한 사람 중에 진실을 아는 사람이 있으면
            can[i] = False # 그 파티는 구라 불가능
            know = know | people # 아는 사람을 그 파티에 있던 사람들까지 포함해서 다시 초기화

result =  0
for i in range(M):
    if can[i]:
        result += 1

print(result)