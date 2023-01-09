# greedy
input = __import__('sys').stdin.readline
money = int(input())

cnt = 0
money = 1000 - money

while money > 0:
    cnt += money // 500
    money = money % 500

    cnt += money // 100
    money = money % 100

    cnt += money // 50
    money = money % 50
    
    cnt += money // 10
    money = money % 10
    
    cnt += money // 5
    money = money % 5
    
    cnt += money // 1
    money = money % 1

print(cnt)

###########쉬운답###########
# a = 1000 - int(input())
# b = [500, 100, 50, 10, 5, 1]
# count = 0
# for i in b:
#     count += a // i
#     a %= i
# print(count)
