letters = input()

croatia_alpha = ["c=","c-","dz=","d-","lj","nj","s=","z="]

for i in croatia_alpha:
    while i in letters:
        letters = letters.replace(i,"1")
        

print(len(letters))

        