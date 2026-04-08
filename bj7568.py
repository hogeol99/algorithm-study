n = int(input())

infor = []
answer = []
for i in range(n):
    infor.append(list(map(int,input().split())))

for j, a in enumerate(infor):
    count = 0
    for k, b in enumerate(infor):
        if j != k and a[0]<b[0] and a[1] < b[1]:
            count += 1
    answer.append(1+count)
print(*answer)

