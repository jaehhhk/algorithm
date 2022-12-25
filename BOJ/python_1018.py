N, M  = map(int, input().split())

chess = []
for i in range(N):  # N 행을 만들어야 하므로
    chess.append(input())

cnt = []
# 8*8 행렬로 잘라야 하는데, index out of range 오류 피하기 위해 7 뺀 상태로 반복문
for x in range(N-7):
    for y in range(M-7):
        white = 0   # w 로 시작할 경우 바뀐 체스판의 개수
        black = 0   # b 로 시작할 경우 바뀐 체스판의 개수
        
        # 이때 white / black 변수는 검은색, 흰색 상관없이 바꿔야 할 체스 타일의 총 개수이다
        for i in range(x, x+8):
            for j in range(y, y+8):
                # 행, 열 좌표의 합이 짝수인지 아닌지 여부에 따라 맨 처음 칸과 같아야 하는지 달라야 하는지 조건이 다름
                if (i + j) % 2 == 0:    # 만약 합이 짝수라면 -> 시작점과 같아야
                    if chess[i][j] != "W":  # B이면
                        white += 1      # w 로 시작하는 체스판의 경우 그 칸이 w가 되어야 하므로(그래야 같아짐) white 에 1 더함
                    else:   # W이면
                        black += 1  # 반대로 black에 1 더함
                else:   # 시작점과 다른 경우
                    if chess[i][j] != "W":
                        black += 1  # b로 시작하는 체스판은 달라야 하므로 white로 칸을 바꿔줘야 한다. 그래서 1 더함
                    else:
                        white += 1
        
        cnt.append(white)
        cnt.append(black)
print(min(cnt))