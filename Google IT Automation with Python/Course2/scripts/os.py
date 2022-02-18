import os

if os.path.exists("spider.txt"):
    os.remove("spider.txt")
else:
    print("Spider file does not exist")

if os.path.exists("f.txt"):
    os.rename("f.txt", "fi.txt")

print(os.path.exists("./fi.txt"))

with open("fi.txt", "a") as file:
    file.write("some text")

print(os.path.getsize("fi.txt"))
timestamp = os.path.getmtime("fi.txt")

import datetime

print(datetime.datetime.fromtimestamp(timestamp))

print(os.path.abspath("fi.txt"))

print(os.getcwd())
if not os.path.exists("new_dir"):
    os.mkdir("new_dir")
os.mkdir("newer_dir")
os.chdir("new_dir")
os.rmdir("../newer_dir")

os.chdir("..")
print(os.listdir("."))

for name in os.listdir("."):
    fullname = os.path.join(".", name)
    if os.path.isdir(fullname):
        print(f"{fullname} is a directory")
    else:
        print(f"{fullname} is a file")

with open("textfile.txt") as txt:
    pass