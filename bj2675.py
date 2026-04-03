n = int(input())

for i in range(n):
    temp, letters =input().split()
    a = int(temp)
    answer = ""
    for j in letters:
        for k in range(a):
            answer+=j
    print(answer)