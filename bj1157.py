letter_cnt = [0]  * (ord('Z') - ord('A') + 1)

letters = input().upper()

for i in letters:
    letter_cnt[ord(i)-ord('A')] += 1


answer = ""
max_value = 0

for j, value in enumerate(letter_cnt):
    if value > max_value:
        max_value = value
        answer = chr(ord('A') + j)
    elif value == max_value:
        answer = "?"
print(answer)

