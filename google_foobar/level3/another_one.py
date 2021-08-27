# the problem is identical to the of the total number of subsets matching a given sum
# given that that starting numbers make up all the numbers starting from 1 up to n-1 exactly once

def subsets(possible_stairs, n):
    # instantiate the final output (exactly one way to bring sum to 0)
    s = [1] + [0] * (n)

    # we want to find all possible sums with the current number
    # i.e. how many ways to make 0 -> 1 (already established in s)
    # ways to make 1 -> 1 ... (since we the input is [1, 2, 3, ..., n-1])
    for current in possible_stairs:
        # start iterating from the target (n)
        for num in range(n, current-1, -1):
            # if it is possible to sum to num, add it to s[num]
            if s[num-current]:
                s[num] += s[num-current]

    # since the input (possible_stairs) does not include n, we do not have to worry about subsets with length < 2
    return s[n]

def solution(n):
    stairs = list(range(1, n))
    return subsets(stairs, n)





# print(solution(3)) # 1
# print(solution(4)) # 1
# print(solution(5)) # 2
print(solution(6)) # 3
# print(solution(7)) # 4
# print(solution(8)) # 5
# print(solution(9)) # 7
# print(solution(10)) # 9

# print(solution(200)) # 487067745