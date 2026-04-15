n = int(input())

for i in range(n):
    data = input()
    vps = 0
    for j in data:
        if j == "(":
            vps += 1
        elif j == ")":
            vps -= 1
            if vps < 0 :
                break
    if vps == 0:
        print("YES")
    else:
        print("NO")

