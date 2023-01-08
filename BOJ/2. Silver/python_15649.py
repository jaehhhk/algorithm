input = __import__('sys').stdin.readline



def go(arr):
    if len(arr) == M:
        print(' '.join(map(str, arr)))
        return
    
    for i in range(N):
        if len(arr) == 0 or li[i] not in arr:
            arr.append(li[i])
            go(arr)
            arr.pop()

N, M = map(int, input().split())
li = []
for i in range(1, N+1):
    li.append(i)
li.sort()
go([])
