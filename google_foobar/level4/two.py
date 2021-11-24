# in order to solve the problem a pattern needs to be established for the pairs that lead to terminating games
# say e.g. trainer_i has m bananas and trainer_j has n bananas. without loss of generality assume that m <= n
# if m == n the game terminates, otherwise at least one game must be played.
# the rule for the game is (a, b) -> (2a, b - a) if a < b and (a, b) -> (a - b, 2b) if a > b and the game ends
# when a == b.
# using this rule we may construct a binary tree of the possible games that can be played (assuming n < m):
# (m, n)
# (2m, n - m)   * only one step due to the assumption
# (4m, n - 3m)  (3m - n, 2n - 2m)
# (8m, n - 7m)  (7m - n, 2n - 6m)   (6m - 2n, 3n - 5m)  (5m - 3n, 4n - 4m)
# ...
#
# focusing on the first term in each of the tuples, we find that a game is terminating whenever
# am - bn == (m + n)/2        -> (m + n odd will always cycle)
# this leads to the equation
# m / n == (2b + 1) / (2a - 1)      (*1)
# it is also clear from the pattern in the binary tree of possible games that a + b == 2 ** i where i is some
# positive integer. using b == 2 ** i - a in (*1) gives:
# (m + n) / n == 2 ** (i+1) / (2a - 1)      (*2)

# (*2) is enough to determine whether a given game will cycle or terminate. all we need to do is find the reduced
# fractional form of (m + n) / n = num / denom and check if num is a power of two.


def pow_of_two(n):
    return (n & -n) == n


def reduced_fraction_numerator(numerator, denominator):
    if numerator == 0:
        return 0
    elif denominator == 0:
        return "NaN"
    else:
        gcd = find_gcd(numerator, denominator)
        return numerator / gcd


def find_gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


def game_will_cycle(m, n):
    p = reduced_fraction_numerator(m + n, n)
    return not pow_of_two(int(p))


def solution(banana_list):
    # the game requires at least two players
    if len(banana_list) == 1:
        return 1

    # # if we sort the list first we can make use of a fact of numbers later for pairing the trainers
    # banana_list = sorted(banana_list)

    terminating_games = {i: {
        "terminating_pairings": [],
        "length": 0
    } for i in range(len(banana_list))}
    for i in range(len(banana_list)):
        for j in range(i):  # only lower triangular points are considered
            m = min(banana_list[i], banana_list[j])
            n = max(banana_list[i], banana_list[j])
            total = m + n
            termination_number = float(total) / 2

            if n == m:
                terminating_games[i]["terminating_pairings"].append(j)
                terminating_games[i]["length"] += 1
            # if the total is odd the game will cycle
            elif total % 2 == 1:
                pass
            # if the termination number is odd there is also no way for the game to end
            elif int(termination_number) % 2 == 1:  # can safely do this since total is even
                pass
            # otherwise we check if the numerator in the reduced fraction is a power of two
            else:
                if not game_will_cycle(m, n):
                    terminating_games[i]["terminating_pairings"].append(j)
                    terminating_games[i]["length"] += 1

    # now we need to pair up trainers such that the most trainers are stuck in infinite games
    # this will be done by pairing the trainers with the most terminating games first

    terminations_by_length = {}
    max_len = 0
    for i in range(len(banana_list)):
        if terminating_games[i]["length"] > max_len:
            max_len = terminating_games[i]["length"]
        if terminating_games[i]["length"] not in terminations_by_length:
            terminations_by_length[terminating_games[i]["length"]] = [i]
        else:
            terminations_by_length[terminating_games[i]["length"]].append(i)

    trainer_pairings = {}
    for i in range(max_len, -1, -1):
        if i not in terminations_by_length:
            continue
        else:
            # construct the pairs by first pairing up those trainers that have the most terminating games
            # start with the highest possible and try to construct a pair for each element j (provided a pair does
            # not already exist)
            for j in terminations_by_length[i]:
                current_level = i
                while current_level >= 0 and j not in trainer_pairings:
                    if current_level not in terminations_by_length:
                        current_level -= 1
                    else:
                        for k in terminations_by_length[current_level]:
                            if j == k:
                                pass
                            elif k not in trainer_pairings and k not in terminating_games[j]["terminating_pairings"]:
                                trainer_pairings[j] = k
                                trainer_pairings[k] = j
                                break
                        current_level -= 1

    print(trainer_pairings)

    return len(banana_list) - len(trainer_pairings)


# print(solution([300]))  # 1
# print(solution([1, 1]))  # 2
# print(solution([1, 7, 3, 21, 13, 19]))  # 0
# print(solution([13, 3]))  # 2
# print(solution([5, 2, 3]))  # 1
# print(solution([3, 5]))  # 2
#
# print(solution([1073741823, 1]))  # 2
# print(solution([1073741823, 2]))  # 0
# print(solution([1, 7, 3, 21, 13, 19, 6, 18, 42]))  # 1
# print(solution([1, 7, 3, 21, 13, 19, 6, 18]))  # 0
# print(solution([1, 7, 3, 21, 13, 19, 63, 1]))  # 0
print(solution([1, 7, 15, 15, 15]))  # 3
print(solution([1, 7, 15, 15, 15, 17, 18]))
# print(solution([1, 7, 15, 15, 15, 17]))  # 2
# print(solution([1064741825, 373741823, 173741823, 1073741823, 1064741825, 334123, 1734823, 10734123, 10644185, 3774123, 17374123, 10737183, 106741825, 37374123, 17374123, 107374183,1064741825, 373741823, 173741823, 1073741823, 1064741825, 334123, 1734823, 10734123, 10644185, 3774123, 17374123, 10737183, 106741825, 37374123, 17374123, 107374183, 1064741825, 373741823, 173741823, 1073741823, 1064741825, 334123, 1734823, 10734123, 10644185, 3774123, 17374123, 10737183, 106741825, 37374123, 17374123, 107374183]))

