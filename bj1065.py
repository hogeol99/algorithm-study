n = int(input())

answer = 0

for i in range(1,n+1):
    if i < 100:
        answer += 1
    else:
        temp = str(i)
        distance = int(temp[0]) - int(temp[1])
        is_pass = 1
        for j in range(len(temp)-1):
            if int(temp[j]) - int(temp[j+1]) != distance:
                is_pass = 0
                break
        if is_pass == 1:
            answer += 1
print(answer)

                

