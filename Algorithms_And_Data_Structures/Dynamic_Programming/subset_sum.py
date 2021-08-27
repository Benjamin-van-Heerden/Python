import numpy as np
def solve_subset(A, M, S):
    for i in range(1, len(A)+1):
        for j in range(1, M+1):
            if S[i-1][j]:
                S[i][j] = S[i-1][j]
            else:
                S[i][j] = S[i-1][j-A[i-1]]

    return S[len(A), M] 
    


A = [5, 2, 1, 0]
M = 9
S = np.array([[True]+[False]*(M) for _ in range(len(A)+1)])
print(solve_subset(A, M, S))