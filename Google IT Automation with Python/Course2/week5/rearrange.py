import re
import sys

def rearrange_name(name):
    result = re.search(r"^([\w.\s]*), ([\w.\s]*)", name)
    if len(name.split()) == 1:
        return name
    elif result is None:
        return None
    return f"{result[2]} {result[1]}"