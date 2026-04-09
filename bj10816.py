from collections import Counter

n = int(input())

cards = list(map(int,input().split()))

cnt = Counter(cards)

m = int(input())

card_list = list(map(int,input().split()))

for i in card_list:
    print(cnt[i],end = " ")
print()
