# 2(1+2)를 2*1 + 2*2로 계산하는 논리 (stack 이용) 
letter = input()

tmp = 1
result = 0
stack = []

for i in range(len(letter)):
    s = letter[i]
    if s == '(':
        tmp *= 2
        stack.append(s)
    elif s == '[':
        tmp *= 3
        stack.append(s)
    
    elif s == ')':
        if not stack or stack[-1] == '[':
            result = 0
            break
        if letter[i-1] == '(':
            result += tmp
        tmp //= 2   # () 점수를 result에 더해줬으므로 tmp에선 원래대로 돌아가야
        stack.pop() # pop 괄호 안에 인덱스 생략하면 마지막 삭제
    else:
        if not stack or stack[-1] == '(':   #(] 인 경우
            result = 0
            break
        if letter[i-1] == '[':
            result += tmp
        
        stack.pop()
        tmp //= 3
if stack:   # 정상적인 경우엔 마지막엔 stack에 값이 있으면 안됨
    print(0)
else:
    print(result)