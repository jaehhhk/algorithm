input = __import__('sys').stdin.readline

n, d = map(int, input().split())
li = []
for i in range(1, n+1):
    li.append(str(i))

ans = 0  
for i in range(len(li)):
    if len(li[i]) == 1:     # 길이가 1인 경우
       if li[i] == str(d):
           ans += 1

    else:       # 길이가 2 이상인 경우 
        for j in range(len(li[i])):
            if li[i][j] == str(d):
                ans += 1
                

print(ans)

