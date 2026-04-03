n, x = map(int, input().split())

numbers = map(int,input().split())

answer = []

for i in numbers:
    if i < x:
        answer.append(i)

print(*answer)