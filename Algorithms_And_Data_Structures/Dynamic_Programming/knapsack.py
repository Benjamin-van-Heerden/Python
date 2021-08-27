import numpy as np

def knapsack(M, w, v, n):
    if n == 0 or M == 0:
        return 0
    # if the item cannot be fit into the knapsack: 
    if w[n-1] > M:
        return knapsack(M, w, v, n-1)
    else:
        # if it can fit we have two options
        n_excluded = knapsack(M, w, v, n-1)
        n_included = v[n-1] + knapsack(M-w[n-1], w, v, n-1)

    return max(n_excluded, n_included)



# M = 5
# w = [4, 2, 3]
# v = [10, 4, 7]
# print(knapsack(M, w, v, 3))

# M = 10
# w = [5, 7, 9, 2]
# v = [10, 13, 19, 4]
# print(knapsack(M, w, v, 4))

def knapsack_dynamic(M, w, v, n, S):
    # we again have two cases, either the item cannot fit or it can
    # if the item cannot be fit into the knapsack: 
    
    for i in range(1, n+1):
        for j in range(1, M+1):
            if w[i-1] > j:
                S[i][j] = S[i-1][j]
            else:
                S[i][j] = max(S[i-1][j], v[i-1] + S[i-1][j-w[i-1]])
    # we want the result in the very last row and column
    print(f"The maximal value for the knapsack is ${S[n, M]}")
    return S

def show_result(S, W):
    w = len(S[0])-1
    for n in range(len(S)-1, 0, -1):
        if S[n, w] != 0 and S[n, w] != S[n-1, w]:
            print(f"We take item #{n}")
            w = w - W[n-1]
    
        

    
print()
M = 5
w = [4, 2, 3]
v = [10, 4, 7]
n = 3
S = np.array([[0]*(M+1)]*(n+1))
S1 = knapsack_dynamic(M, w, v, n, S)
show_result(S1, w)
print()

M = 10
w = [5, 7, 9, 2]
v = [10, 13, 19, 4]
n = 4
S = np.array([[0]*(M+1)]*(n+1))
S1 = knapsack_dynamic(M, w, v, n, S)
show_result(S1, w)
print()

M = 1
w = [5, 7, 9, 2]
v = [10, 13, 19, 4]
n = 4
S = np.array([[0]*(M+1)]*(n+1))
S1 = knapsack_dynamic(M, w, v, n, S)
show_result(S1, w)
print()

