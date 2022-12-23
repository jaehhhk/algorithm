players = int(input())

games = []
for i in range(players):
    games.append(list(map(int, input().split())))

# 2차원 배열 x,y 변경 -> 게임 참가자를 기준으로 구조 변경
games_modified = [[] for _ in range(3)]
for i in range(3):
    for j in range(players):
        games_modified[i].append(games[j][i])

# 중복 여부를 점수로 반영한 결과값 저장
result = [[] for _ in range(players)]
for i in range(3):
    for j in range(players):
        if list(games_modified[i]).count(games_modified[i][j]) > 1 :    # 자신과 같은 값이 있다는 이야기는 1게임에 같은 값이 2개 이상이라는 뜻
            result[j].append(0) # 자신을 제외하고 같은 값이 있을 경우 0점
        elif list(games_modified[i]).count(games_modified[i][j]) == 1: 
            result[j].append(games_modified[i][j])

# 결과 구하기
for i in range(players):
    print(sum(result[i]))       