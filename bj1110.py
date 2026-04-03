n = int(input())


answer = 0

temp = n

while True:
    answer += 1
    a = temp//10
    b = temp%10

    temp = b*10 + (a+b)%10

    if n == temp:
        break
print(answer)


