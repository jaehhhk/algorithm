input = __import__('sys').stdin.readline
N = int(input())
taste = list(map(int, input().split()))
k = int(input())

res = []

for i in range(0,N,N//k):
    li = []
    li = taste[i:i+N//k]
    li.sort()
    res.append(li)

for i in res:
    for j in i:
        print(j, end=' ')