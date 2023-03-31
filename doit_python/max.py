# 실습 1-1 15p
# 세 정수의 최댓값 구하기

a = int(input('a 값 입력 :'))
b = int(input('b 값 입력 :'))
c = int(input('c 값 입력 :'))

max = a

if b > max:
    max = b
if c > max:
    max = c
    
print(f'최댓값: {max}')

