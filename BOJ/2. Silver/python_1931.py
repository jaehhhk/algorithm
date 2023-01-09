# greedy
input = __import__('sys').stdin.readline

N = int(input())

table = []
for i in range(N):
    table.append(list(map(int, input().split())))

# 끝나는 시간, 시작 시간 순서대로 오름차순 정렬
table.sort(key = lambda x: (x[1], x[0]))

cnt = 1
end = table[0][1]   # 맨처음은 무조건 끝나는 시간이 제일 빠른 회의가 와야함. 그 뒤로는 시작시간이 제일 빠른 것들 오면된다.
for i in range(1, N):
    if table[i][0] >= end:
        cnt += 1
        end = table[i][1]
        
print(cnt)
