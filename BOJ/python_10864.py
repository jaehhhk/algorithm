N, M = map(int, input().split())    # 학생수 입력 받기

friend = [[] for _ in range(N)]   # 친구관계 저장할 2차원 리스트 정의

for i in range(M):
    a, b = map(int,input().split())
    a -= 1  # 인덱스는 0부터 시작하므로 학생별 인덱스 표현은 1씩 빼주고 시작
    b -= 1
    friend[a].append(b) # a 에게는 b 친구관계
    friend[b].append(a) # b 에게는 a 친구관계

for i in range(N):
    print(len(friend[i]))
