#!/usr/bin/python3
import sys
import string

def character_frequency(filename):
    try:
        f = open(filename)
    except Exception as e:
        print(e)
        return None

    characters = {}
    for line in f:
        for c in line:
            if c in string.punctuation or c == ' ' or c == '\n':
                continue
            if c not in characters:
                characters[c] = 0
            characters[c] += 1
    f.close()
    return characters

if __name__ == "__main__":
    filename = sys.argv[1]
    print(character_frequency(filename))