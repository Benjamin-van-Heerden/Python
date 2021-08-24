import numpy as np

def rod_cuting_dynamic(N, rod_lengths, rod_prices):
    S = np.zeros((len(rod_lengths)+1, N+1))
    
    for i in range(1, len(rod_lengths)+1):
        for j in range(1, N+1):
            if i <= j:
                S[i, j] = max(S[i-1, j], rod_prices[i-1] + S[i][j-i])
            else:
                S[i, j] = S[i-1, j]
    
    print()
    print(f"The optimal cutting will yield ${S[-1, -1]}")
    return S

def print_rods(S, rod_lengths):
    print()
    l = len(S[0])-1
    n = len(S)-1
    while n >= 0:
        if S[n, l] != 0 and S[n, l] != S[n-1, l]:
            print(f"Cut one rod with length {n}")
            l = l - rod_lengths[n-1]
            n += 1
        n -= 1
    print()



N = 5
rod_lengths = [1, 2, 3, 4, 5]
rod_prices = [2, 5, 7, 3, 9]

print_rods(rod_cuting_dynamic(N, rod_lengths, rod_prices), rod_lengths)

N = 5
rod_lengths = [1, 2, 3, 4, 5]
rod_prices = [2, 5, 7, 3, 20]

print_rods(rod_cuting_dynamic(N, rod_lengths, rod_prices), rod_lengths)

N = 5
rod_lengths = [1, 2, 3, 4, 5]
rod_prices = [7, 5, 7, 3, 20]

print_rods(rod_cuting_dynamic(N, rod_lengths, rod_prices), rod_lengths)



    


    