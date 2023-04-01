# +와 -번갈아 출력하기

print('+와 - 번갈아 출력하기')

n = int(input('몇개 출력할 지 입력: '))

for i in range(n):
    if i % 2:   #홀수인 경우
        print('-', end='')
    else:       #짝수인 경우
        print('+', end='')
        