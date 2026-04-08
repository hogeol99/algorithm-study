n = int(input())

cards1 = set(map(int,input().split()))

m =int(input())

cards2 = list(map(int,input().split()))


for i in cards2:
    if i in cards1:
        print(1,end= " ")
    else:
        print(0, end = " ")
print()