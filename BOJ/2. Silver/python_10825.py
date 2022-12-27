N = int(input())

student = []
for i in range(N):
    name, a, b, c = input().split()
    student.append([name, int(a), int(b), int(c)])

student = sorted(student, key = lambda stdnt: [-stdnt[1], stdnt[2], -stdnt[3], stdnt[0]])

for i in range(N):
    print(student[i][0])