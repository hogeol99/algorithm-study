kg = int(input())

answer = 0

answer += kg//15 * 3

kg = kg%15

if kg == 1 or kg == 2 or kg == 4 or kg == 7 or kg == 14:
    answer = -1
elif kg == 3 or kg == 5:
    answer += 1
elif kg == 6 or kg ==10 or kg == 8:
    answer += 2
elif kg ==9 or kg == 13 or kg == 11:
    answer += 3
elif kg == 12:
    answer += 4
print(answer)