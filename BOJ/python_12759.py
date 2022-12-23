# 게임판에 o,x 표시 -> 가로, 세로, 대각선 라인별 세트로 받아오기 -> 같은 문자 연속으로 3개 나온 문자의 플레이어가 승리
start  = int(input())

game = [[' '] * 3 for _ in range(3)]

while 1:    # for문쓰기 애매하면 while문 써준다
    # 게임 시작, o/x 적어주면서 진행
    x, y = map(int, input().split())
    x -= 1  # 인덱스는 0부터 시작하므로 1씩 빼주기
    y -= 1

    winner = 0
    
    if start == 1:
        game[x][y] = 'O'
    else: game[x][y] = 'X'
    
    # 연속된 문자 3개 나오는지 확인
    result = []
    for i in range(3):
        result.append([game[i][0], game[i][1], game[i][2]]) # 가로줄
        
    for i in range(3):
        result.append([game[0][i], game[1][i], game[2][i]]) # 세로줄
        
    result.append([game[0][0], game[1][1], game[2][2]]) # 대각선
    result.append([game[0][2], game[1][1], game[2][0]]) # 반대 대각선
    
    if ['O', 'O', 'O'] in result:
        winner = 1
    if ['X', 'X', 'X'] in result:
        winner = 2
    
    if winner == 0:
        temp = False
        for i in range(len(result)):
            if ' ' in result[i]:
                temp = True
        if not temp: winner = 3
    
    # 승부 정해질 때
    if winner >0:
        break
    
    # 턴을 넘기기(시작 누구부터 했는지에 따라 if문)
    if start == 1:
        start = 2
    else:
        start = 1

if winner < 3:
    print(winner)
else:   # 비긴 경우
    print(0)
    
    
    
    
    
     
    
    
