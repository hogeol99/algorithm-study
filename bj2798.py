n , m = map(int,input().split())

cards = list(map(int,input().split()))

answer = 0

for i, v1 in enumerate(cards):
    for j, v2 in enumerate(cards):
        for k, v3 in enumerate(cards):
            if i != j and i != k and j != k and v1+v2+v3 > answer and v1+v2+v3 <=m:
                answer = v1+v2+v3

print(answer)

