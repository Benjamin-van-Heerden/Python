def iterationSum(n):
    result = 0
    for i in range(n+1):
        result += i
    return result

print(iterationSum(3))

def recursionSum(n):
    if n <= 1:
        return 1
    else:
        return n + recursionSum(n-1)

print(recursionSum(3))

