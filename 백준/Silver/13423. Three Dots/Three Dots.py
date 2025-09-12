# Three Dots
import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N = int(input())
    dots = list(map(int, input().split()))
    dots.sort()
    result = 0

    # 모든 중간 점을 기준으로 나머지 두 개 위치를 결정
    for j in range(1, N-1):
        left, right = 0, N-1
        while left < j and right > j:
            if dots[left] + dots[right] == 2 * dots[j]:
                result += 1
                left += 1
                right -= 1
            elif dots[left] + dots[right] < 2 * dots[j]:
                left += 1
            else:
                right -= 1
                
    print(result)