N = int(input())

paper = [list(map(int, input().split())) for _ in range(N)]
result = {"-1": 0, "0": 0, "1": 0}

def recursion(N, paper):
    first = paper[0][0]  # 현재 영역의 첫 번째 값
    for i in range(N):
        for j in range(N):
            if paper[i][j] != first:  # 현재 영역에 다른 값이 있는 경우
                # 3x3으로 나눈 후 각각의 부분에 대해 재귀 호출
                for x in range(3):
                    for y in range(3):
                        new_paper = []
                        for row in paper[x * (N // 3):(x + 1) * (N // 3)]:
                            new_paper.append(row[y * (N // 3):(y + 1) * (N // 3)])
                        recursion(N // 3, new_paper)
                return

    # 모든 값이 같을 경우
    result[str(first)] += 1

# 초기 호출
recursion(N, paper)

# 결과 출력
print(result["-1"])
print(result["0"])
print(result["1"])