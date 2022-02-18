def reverse_integer(i):
    return int(str(i)[::-1])

# can do it with modulo operations as well. This is cleaner and also O(N)
def another_reverse_integer(n):
    reversed = 0
    remainder = 0
    while n > 0:
        remainder = n % 10
        reversed = reversed*10 + remainder
        n = n // 10
    return reversed


print(reverse_integer(1234))
print(another_reverse_integer(1234))