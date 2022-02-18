#!/usr/bin/python3

import sys

def is_valid_username(username, minlen):
    assert type(username) == str, "username must be a string"

    if minlen < 1:
        raise ValueError("minlen must be at least one")
    if len(username) < minlen:
        return False
    if not username.isalnum():
        return False
    return True

if __name__ == "__main__":
    username = sys.argv[1]
    minlen = int(sys.argv[2])

    print(is_valid_username(username, minlen))