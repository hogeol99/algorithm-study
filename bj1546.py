n = int(input())

scores = list(map(float,input().split()))

max_score = max(scores)
total = 0.0

for i in range(len(scores)):
    total += scores[i] / max_score * 100
print(total/len(scores))
