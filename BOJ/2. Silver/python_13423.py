from collections import defaultdict
input = __import__('sys').stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    li = sorted(list(map(int, input().split())))
    
    spotList = defaultdict(int) # defautdict모듈 불러와서 int형으로 초기화
    
    for i in range(len(li)):
        spotList[li[i]] = 1        #value값 1(True)로 초기화
    
    ans = 0
    for i in range(n-1):    # i와 j 한 칸 차이나게 뽑아서 비교하기 위해
        for j in range(i+1, n):
            first = li[i]
            second = li[j]
            third = li[j] + (li[j] - li[i])     # 임의의 세 번째 점은 첫 번째 점에서 두 번째 점 사이 거리만큼 두 번째 점에서 떨어져 있어야 등간격
            
            if spotList[third] == 1:    # 그러한 세 번째 점이 딕셔너리 내에 존재하면(True) ans에 1 더함
                ans += 1
    print(ans)