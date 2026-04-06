n = int(input())

answer = 0

for i in range(n):
    letters = input()

    visited = [False] * (ord('z')- ord('a')+1)

    now = ""

    result = True

    for j in letters:
        if now != j:
            now = j
            if visited[ord(j) - ord('a')]:
                result = False
                break
            else:
                visited[ord(j) - ord('a')] = True
    if result:
        answer +=1
        
print(answer)