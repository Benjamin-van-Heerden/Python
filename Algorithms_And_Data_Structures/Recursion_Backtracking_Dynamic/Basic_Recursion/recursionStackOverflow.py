import sys
sys.setrecursionlimit(15000)

import time

def factorialHead(n):
    if n <= 1: 
        return 1
    else: 
        return n * factorialHead(n - 1)

print("Head Recursion:")
now = time.time()
factorialHead(10000) # this should break as I understand - stackoverflow (seems to work fine??)
print(time.time() - now)

def factorialTail(n, currentValue = 1):
    if n <= 1: 
        return currentValue
    else:
        return factorialTail(n-1, n*currentValue)

print("Tail Recursion:")
now = time.time()
factorialTail(10000)
print(time.time() - now)

# Output:
# Head Recursion:
# 0.02311873435974121
# Tail Recursion:
# 0.05035591125488281

#Switched Order
# Tail Recursion:
# 0.05422401428222656
# Head Recursion:
# 0.017311573028564453
