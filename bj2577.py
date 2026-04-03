a = int(input())
b = int(input())
c = int(input())

n = str(a*b*c)

answer = [0]*10

for i in n:
    answer[int(i)] += 1

for j in answer:
    print(j)
