def reverse_array(arr):
    new = [*arr]
    i = 0
    j = len(new)-1
    while i < j:
        new[i], new[j] = new[j], new[i]
        i += 1
        j -= 1
    return new

def is_palindrome(word):
    word_arr = [c for c in word]
    word_arr_rev = reverse_array(word_arr)
    reversed_word = "".join(word_arr_rev)
    return word == reversed_word

def alternative_better_is_palindrome(s):
    return s == s[::-1]


print(is_palindrome("radar"))
print(is_palindrome("madam"))
print(is_palindrome("hello"))
print()
print(alternative_better_is_palindrome("radar"))
print(alternative_better_is_palindrome("madam"))
print(alternative_better_is_palindrome("hello"))