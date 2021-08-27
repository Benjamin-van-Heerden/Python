def fibonacci_recursion(n):
    if n == 0:
        return 0
    if n == 1:
        return 1

    return fibonacci_recursion(n-1) + fibonacci_recursion(n-2)

# cannot handle much more than 40
# print(fibonacci_recursion(40))


# top-down approach
def fibonacci_memoization(n, table={0: 0, 1: 1}):

    if n not in table:
        table[n] = fibonacci_memoization(n-1, table) + fibonacci_memoization(n-2, table)
    
    return table[n]
        
# this can handle very large numbers
print(fibonacci_memoization(900))

# bottom-up approach
def fibonacci_tabulation(n, table={0: 0, 1: 1}):
    for i in range(2, n+1):
        table[i] = table[i-1] + table[i-2]
    return table[n]

print(fibonacci_tabulation(900))



