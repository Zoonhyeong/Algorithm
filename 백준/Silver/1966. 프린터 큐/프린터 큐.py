import sys
from collections import deque
input = sys.stdin.readline

T = int(input())

for _ in range(T):

    N, M = map(int, input().split())
    Q = deque(list(map(int, input().split())))
    
    if N == 1:
        print(1)
    else:
        cnt = 0
        
        while Q:
            elem = Q.popleft()
            
            if Q and max(Q) > elem:
                Q.append(elem)
            else:
                cnt += 1
                if M == 0:
                    break
            M = (M-1) % len(Q)
                    
        print(cnt)