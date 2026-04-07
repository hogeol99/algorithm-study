n = int(input())


answer = 0

for i in range(n):
    temp = i
    temp += sum(map(int,str(i)))
    if temp == n :
        answer = i
        break
print(answer)