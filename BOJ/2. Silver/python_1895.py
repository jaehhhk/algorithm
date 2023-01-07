input = __import__('sys').stdin.readline

R, C = map(int, input().split())

image = []
for i in range(R):
    image.append(list(map(int, input().split())))

T  = int(input())

cnt = 0

for i in range(R-2):
    for j in range(C-2):
        pix = []
        for k in range(i, i+3):
            for l in range(j, j+3):
                pix.append(image[k][l])
        pix.sort()
        
        if pix[4] >= T:
            cnt += 1
        
print(cnt)