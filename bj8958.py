n = int(input())

for i in range(n):
    result = input()
    score = 0
    sequence = 0
    for j in result:
        if j == 'O':
            sequence += 1
            score += sequence
        elif j == 'X':
            sequence = 0
    print(score)
