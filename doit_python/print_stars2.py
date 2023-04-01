# *를 n개 출력하되 w마다 줄바꿈하기 효율적인 버전

print('*를 출력')
n = int(input('몇개 출력?: '))
w = int(input('몇개마다 줄바꿈?: '))

for _ in range(n // w):     # 아예 한줄씩 세트로 묶에 출력
    print('*' * w)

# 나머지에 대해서만 if문 -> if문 판단 1번
rest = n % w
if rest:    # n이 w로 나눠떨어지지 않는 경우 남은 갯수만큼만 마지막에 출력해야
    print('*' * rest)
