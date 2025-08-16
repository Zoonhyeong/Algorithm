import sys

input = sys.stdin.readline

N = int(input())
want_money = list(map(int, input().split()))
total_money = int(input())

want_money.sort()

left, right = 0, want_money[-1]
result = 0

while left <= right:
    mid = (left + right) // 2
    current_sum = 0
    for money in want_money:
        current_sum += min(money, mid)
    
    if current_sum <= total_money:
        result = mid
        left = mid + 1
    else:
        right = mid - 1
    
print(result)