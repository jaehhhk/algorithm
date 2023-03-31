input = __import__('sys').stdin.readline

A_num = input().rstrip()
B_num = input().rstrip()

A = []
B = []

for i in range(len(A_num)):
    A.append(int(A_num[i]))
    B.append(int(B_num[i]))

num = []
for i in range(len(A)):
    num.append(A[i])
    num.append(B[i])

new = []
for i in range(len(num)):
    if i < len(num):
        temp = 0
        temp = num[i] + num[i+1]
        new.append(temp)
    else: break
    num = []
    num = new
    print(num)



# first = A[0] + B[0]
# if first > 9:
#     first = str(first)
#     first = int(first[-1])
# new.append(first)
    
# for i in range(1,8):
#     temp = 0
#     temp = A[i] + B[i]
    
#     if temp > 9:
#         temp = str(temp)
#         temp = int(temp[-1])
    
#     new.append(temp)

# print(new)
    