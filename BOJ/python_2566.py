# 빈 리스트 생성
num_list = []

# 수 입력 받고 빈 리스트에 요소들 넣어주기
for i in range(9):
    num_list.append(list(map(int, input().split())))
    
# for문으로 라인별로 돌면서 최댓값 인자 + 인덱스 찾기
max_list = []
index_list = []
for i in range(9):
    max_list.append(max(num_list[i]))   # 각 라인별 최댓값
    max_value = max(max_list)   # 최종 최댓값

for i in range(9):
    if max_value in num_list[i]:
        temp = list(num_list[i])    # num_list의 한 요소는 리스트가 아님. index 메서드 이용을 위해 임시로 만들어줌
        max_x = i + 1   # 인덱스는 0부터 시작하므로 출력 형식 맞춰주기 위해 1 더함
        max_y = temp.index(max_value) + 1

print(max_value)
print(max_x, max_y, end= " ")
