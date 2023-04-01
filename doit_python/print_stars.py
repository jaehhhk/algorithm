# *을 n개 출력하되 w개마다 줄바꿈하기1 42p

print('* 출력')
n = int(input('몇개 출력?: '))
w = int(input('몇개마다 줄바꿈?: '))

for i in range(n):
    print('*', end='')
    
    if i % w == w-1:    
        print()     # 줄 바꾼다는 뜻
        
if n % w:
    print()
    

############################################################

# 이 코드는 if문을 n번 수행하므로 비효율적
# 수정된 코드는 print_stars2.py
    