N = int(input())

words = []
for _ in range(N):
    words.append(input())

words = set(words)

words = sorted(words, key = lambda s: [len(s), s])  # 문제 말고 출력 양식 부분에도 제약조건 나와있을 수 있다. 

for i in range(len(words)):
    print(words[i])