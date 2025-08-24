import sys
input = sys.stdin.readline

def find(n):
    if parent[n] != n:
        parent[n] = find(parent[n])
    return parent[n]

def union(a, b):
    a = find(a)
    b = find(b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

while True:
    m, n = map(int, input().split())
    if m == 0 and n == 0:
        break  # 종료 조건
    
    parent = [i for i in range(m+1)]
    edges = []
    for _ in range(n):
        x, y, z = map(int, input().split())
        edges.append((x, y, z))
    edges.sort(key=lambda x: x[2])

    answer = 0
    for a, b, c in edges:
        if find(a) == find(b):
            answer += c
        else:
            union(a, b)
    
    # 마지막 두 정수는 추가로 입력받는게 아니라, 이미 입력 후 while 문의 조건으로 끝남
    # 기존 코드 처럼 마지막에 `a, b = map(int, input().split())` 필요 없음
    print(answer)