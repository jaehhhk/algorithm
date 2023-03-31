# 세 정수를 입력받아 중앙값 구하기

def med3(a, b, c):
    if a >= b:
        if b >= c:
            return b
        elif a <= c:
            return a
        else:
            return c
    elif a > c:
        return a
    elif b > c:
        return c
    else:
        return b

a = int(input('a 입력: '))
b = int(input('b 입력: '))
c = int(input('c 입력: '))

print(f'중앙값: {med3(a,b,c)}')