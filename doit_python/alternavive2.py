# alternative1.py의 문제점 해결

# +와 - 번갈아 출력하기

print('+와 - 번갈아 출력')
n = int(input('몇개를 출력?: '))

for _ in range(n//2):
    print('+-', end='')     #일단 +- 세트 묶어서 출력

if n%2:
    print('+', end='')      # n이 홀수면 마지막에 +가 나와야 하므로 추가
    
# 이렇게 하면 if문 한번만 돌면 되므로 효율적