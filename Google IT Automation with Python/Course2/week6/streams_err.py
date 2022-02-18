#!/usr/bin/python3

data = input("This comes from STDIN: ")
print("Now we write to STDOUT: " + data)
raise ValueError("Now we generate an error to STDERROR")