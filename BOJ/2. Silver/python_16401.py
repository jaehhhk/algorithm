input = __import__('sys').stdin.readline

M, N = map(int, input().split())

li = list(map(int, input().split()))

start = 1
end = max(li)

while start <= end:
    mid = (start + end)//2
    tmp = 0
    for i in li:
        tmp += i // mid
    
    if tmp >= M:
        start = mid + 1
    else:
        end = mid -1

print(end)