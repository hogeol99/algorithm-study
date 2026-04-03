numbers = []

answer = 0

max_v = 0

for i in range(9):
    n = int(input())
    if n > max_v:
        max_v = n
        answer = i+1
print(max_v)
print(answer)