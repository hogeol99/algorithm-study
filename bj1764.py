n , m = map(int,input().split())

list1 = set([])
list2 = set([])

for i in range(n):
    list1.add(input())
for j in range(m):
    list2.add(input())

answer = sorted((list)(list1.intersection(list2)))

print(len(answer))
for i in answer:
    print(i)