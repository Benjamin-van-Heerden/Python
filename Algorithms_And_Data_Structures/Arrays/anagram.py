def is_anagram(s, target):
    if len(s) != len(target):
        return False

    s_map = {}
    target_map = {}

    for c in s:
        if c in s_map:
            s_map[c] += 1
        else:
            s_map[c] = 1

    for c in target:
        if c in target_map:
            target_map[c] += 1
        else:
            target_map[c] = 1

    
    for k in s_map.keys():
        if k not in target_map:
            return False
        elif s_map[k] != target_map[k]:
            return False

    return True

# The above is O(N), but relies on dictionaries

def another_is_anagram(s, target):
    if len(s) != len(target):
        return False

    str1 = sorted(s)
    str2 = sorted(target)

    for i in range(len(str1)):
        if str1[i] != str2[i]:
            return False

    return True
    
# this is O(NlogN) at best since we have to sort the arrays

print(is_anagram("restful", "fluster"))
print(is_anagram("restfup", "fluster"))
print(is_anagram("a", "bc"))
print()
print(another_is_anagram("restful", "fluster"))
print(another_is_anagram("restfup", "fluster"))
print(another_is_anagram("a", "bc"))