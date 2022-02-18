import re

with open("text.txt", "r") as f:
    lines = f.readlines()

long_string = "first, last K-krab. So\nFirst, Last M."
string = 'Azerbajana'

result = re.findall(r"([\w. -]+), ([\w. -]+)", long_string)

print(result)