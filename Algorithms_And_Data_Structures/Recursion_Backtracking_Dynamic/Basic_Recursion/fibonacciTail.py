import sys
sys.setrecursionlimit(100000)

def fibTail(n, fib1=0, fib2=1):
    if n == 0:
        return fib1
    elif n == 1:
        return fib2
    else:
        return fibTail(n-1, fib2, fib1 + fib2)

print(fibTail(10000))
