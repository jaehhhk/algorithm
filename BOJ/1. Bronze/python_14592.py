N = int(input())

score = []
for i in range(N):
    S, C, L = map(int, input().split())
    score.append([S, C, L, i+1])

score = sorted(score, key = lambda x: [-x[0], x[1], x[2]])  # 큰게 1등이 되려면 내림차순이므로 앞에 - 붙여야

print(score[0][3])