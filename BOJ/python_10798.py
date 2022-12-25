import sys

letters = []
length = []
for i in range(5):
    letters.append(list(sys.stdin.readline().rstrip()))
    length.append(len(letters[i]))

max_length = max(length)

result = ''
for i in range(max_length):
    for j in range(5):
        if i < length[j]:   # 최대길이보다 길면 다음칸으로 넘어가야
            result += letters[j][i]
print(result)          