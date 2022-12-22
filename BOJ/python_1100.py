# 말 위치 입력받기      
horses = []
for i in range(8):
  horses.append(list(input().split()))

# 짝수번째 줄은 흰색이 먼저, 홀수번째 줄은 검은색이 먼저 배치
cnt = 0
for i in range(8):
    if i % 2 == 0:  # 짝수줄인 경우
        for j in range(8):
            if j % 2 == 0:
                if horses[i][0][j] == "F":  # 2차원 리스트의 요소 하나하나는 ''로 감싸진 하나의 문자열 -> 문자열 인덱싱을 해야하므로[0]이 중간에 낀 것
                    cnt += 1
    else:   # 홀수줄인 경우
        for j in range(8):
            if j % 2 == 1:
                if horses[i][0][j] == "F":
                    cnt += 1

print(cnt)
