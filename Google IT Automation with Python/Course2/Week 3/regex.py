with open("text.txt", "r") as f:
    lines = f.readlines()
    f.close()

words = []
lines = [l.split() for l in lines]
for l in lines:
    for w in l:
        words.append(w)


with open("text.txt", "w") as f:
    for w in words:
        f.write(w+'\n')

