# 5등과 패널티 차이로 수상 못한 학생에게만(6등부터 카운팅 시작)

N = int(input())

student = []
for i in range(N):
    student.append(list(map(int, input().split())))

student = sorted(student, key = lambda x: [-x[0], x[1]])

cnt = 0

if N == 5:
    cnt = 0
else:
    for i in range(1, N-4): # out of range 오류 피하기 위해 '-' 이용하여 인덱싱
        if student[-i][0] == student[4][0]: # 5등과 등수가 같은 경우에만 카운팅
            cnt += 1

print(cnt)
