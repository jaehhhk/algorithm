# 말 위치 입력받기      
horses = []
for i in range(8):
  horses.append(list(input().split()))

# 홀수번째 줄은 흰색이 먼저, 짝수번째 줄은 검은색이 먼저 배치
cnt = 0
for i in range(8):
    # 리스트 인덱스는 0부터 시작하므로 홀수, 짝수 개념 반대로 바뀜
    if i % 2 == 0:  # 홀수줄인 경우
        for j in range(8):
            if j % 2 == 0:
                if horses[i][0][j] == "F":
                    cnt += 1
    else:   # 짝수줄인 경우
        for j in range(8):
            if j % 2 == 1:
                if horses[i][0][j] == "F":
                    cnt += 1

print(cnt)
