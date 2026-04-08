n = int(input())

answer = 666

now = 0

while True:
    if "666" in str(answer):
        now += 1
    if now == n:
        print(answer)
        break
    answer+=1
