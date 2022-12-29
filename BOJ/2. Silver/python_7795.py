# 이분탐색법으로 풀어야 정답 -> 다시 풀어보기
from sys import stdin
T = int(stdin.readline())


for _ in range(T):
    cnt = 0
    
    N, M = map(int, stdin.readline().split())

    A = list(map(int, stdin.readline().split()))
    B = list(map(int, stdin.readline().split()))
    
    A.sort()
    B.sort()
    
    for i in A:
        for j in B:
            if i > j:
                cnt += 1
            else:
                break
    
    print(cnt)