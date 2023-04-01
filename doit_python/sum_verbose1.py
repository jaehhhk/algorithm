# a부터 b까지 정수합 구하기 38페이지

a = int(input('a 값: '))
b = int(input('b 값: '))

# 오름차순 정리
if a > b:
    a, b = b, a
    
sum  = 0

## 비추
# for i in range(a, b+1): # range(a, b+1)은 a이상 b+1미만이므로
#     if i < b:
#         print(f'{i} + ', end = " ")     # 진행중인 값
#     else:
#         print(f'{i} = ', end = " ")     # 최종값. 수 뒤에 = 출력
#     sum += i
    
# print(sum)  # 결과값. = 뒤에 나오는 최종 연산 결과값

for i in range(a, b):
    print(f'{i} + ', end=" ")
    sum += i
    
print(f'{b} = ', end=' ')   # 마지막 부분 ... + b = 
sum += b    # 반복문에서 계속 i 더해주던 수에서 마지막 수인 b 하나만 더 더해주고 끝
    
print(sum)
