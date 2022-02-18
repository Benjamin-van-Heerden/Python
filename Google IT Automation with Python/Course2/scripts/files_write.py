with open("spider.txt", "r+") as file:
    file.write("some new text\n")
    print(file.readlines())