file = open("spider.txt")
print(file.readline())
print(file.read())
file.close()
print()

with open("spider.txt") as file:
    for line in file:
        print(line.upper().strip())

with open("spider.txt") as file:
    file_ = file.readlines()

print(file_)