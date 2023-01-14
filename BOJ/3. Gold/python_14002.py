input = __import__('sys').stdin.readline

N = int(input())
li = list(map(int, input().split()))
dp = [1 for i in range(N)]

res = []
for i in range(N):
    for j in range(i):
        if li[i] > li[j]:
            dp[i] = max(dp[i], dp[j]+1)

print(max(dp))

std = max(dp)
for i in range(N-1, -1, -1):
    if dp[i] == std:
        res.append(li[i])
        std -= 1


for i in res[::-1]:
    print(i, end = " ")
