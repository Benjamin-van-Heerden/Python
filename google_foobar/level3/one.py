# the crux of this problem lies with the heights of the stairs that can be constructed.
# they next set of stairs must be derived from the previous set and must sum to n
# when constructing new stairs we can place brics only on the "columns" that already exist
# this is nearly identical to the subset sum problem provided the length of the subset is at least two

def helper_solution(n, s):
    if n <= 4:
        return s[n]
    
    for i in range(4, n):
        s[i+1] = []
        for j in range(len(s[i])):
            stair_struc = s[i][j]
            stair_length = len(stair_struc)-1
            for col_index, col_value in enumerate(stair_struc):
                if col_index == 0:
                    new_stair = [col_value+1] + stair_struc[1:]
                elif (col_index == stair_length and stair_struc[col_index-1] - col_value > 1):
                    new_stair = stair_struc[:-1] + [col_value+1, 0]
                elif (stair_struc[col_index-1] - col_value > 1):
                    new_stair = stair_struc[:col_index] + [col_value+1] + stair_struc[col_index+1:]
                else:
                    new_stair = []
                if new_stair and new_stair not in s[i+1]:
                    s[i+1].append(new_stair)               


    return s[n]


    


    

def solution(n):
    return len(helper_solution(n, {3:[[2, 1, 0]], 4:[[3, 1, 0]]}))





print(solution(3)) # 1
print(solution(4)) # 1
print(solution(5)) # 2
print(solution(6)) # 3
print(solution(7)) # 4
print(solution(8)) # 5
print(solution(9)) # 7

# print(solution(200)) # 487067745