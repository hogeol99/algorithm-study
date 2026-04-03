n = int(input())

for i in range(n):
    scores = list(map(float,input().split()))
    total = 0.0
    students_count = len(scores)-1
    for j in scores[1:]:
        total += j
    mean_score = total/students_count

    elite_students_count = 0
    for j in scores[1:]:
        if j > mean_score:
            elite_students_count += 1
    print("{:.3f}%".format(elite_students_count/students_count*100))

