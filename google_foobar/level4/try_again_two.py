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

# that was the easy part, what we are left with is a matrix representation of the games that will cycle. we would like
# to maximise the number of games that will cycle, which amounts to maximizing the edge weight in the graph that is
# created. this amounts to a problem of finding the maximum matching for a non-bipartite graph. this is achieved by
# recursively finding augmenting paths for the current matching until all vertices have been considered and no
# augmenting paths remain

from fractions import gcd


def game_will_cycle(m, n):
    num = (m + n) // gcd(m, n)
    return not (num & -num) == num


def solution(banana_list):
    # require at least two trainers for games to be played
    if len(banana_list) == 1:
        return 1

    # construct a boolean matrix representing the games that can cycle
    cyclic_games_adj_matrix = [[game_will_cycle(i, j) for i in banana_list] for j in banana_list]

    # initially all the vertices are unmatched
    matched_vertices = [-1] * len(banana_list)
    pairings = 0
    for i in range(len(banana_list)):
        # we consider every vertex as unvisited on each iteration
        visited = [False] * len(banana_list)
        if possible_pairing(cyclic_games_adj_matrix, i, matched_vertices, visited):
            pairings += 1

    # pairings may not be odd (this amounts to a "dangling vertex")
    if pairings % 2 == 1:
        pairings -= 1

    return len(banana_list) - pairings


def possible_pairing(graph, source, matched_vertices, visited):
    for i in range(len(graph)):
        if graph[source][i] and not visited[i]:
            visited[i] = True
            # if the vertex we are considering is unmatched (i) OR it can be matched to another vertex given
            # the list of seen vertices, update the matching of the current vertex to the source
            # the action here is similar to that of a breadth-first-search for augmenting paths, then updating
            # the matched vertices if such a path is found. since the algorithm tracks if matched_vertices[i] == -1
            # there may be dangling vertices which need to be removed
            if matched_vertices[i] == -1 or possible_pairing(graph, matched_vertices[i], matched_vertices, visited):
                matched_vertices[i] = source
                return True
    return False

print(solution([300]))  # 1
print(solution([1, 1]))  # 2
print(solution([1, 7, 3, 21, 13, 19]))  # 0
print(solution([1, 3, 7, 15]))  # 2
print(solution([13, 3]))  # 2
print(solution([5, 2, 3]))  # 1
# print(solution([3, 5]))  # 2
# #
# print(solution([1073741823, 1]))  # 2
# print(solution([1073741823, 2]))  # 0
# print(solution([1, 7, 3, 21, 13, 19, 6, 18, 42]))  # 1
# print(solution([1, 7, 3, 21, 13, 19, 6, 18]))  # 0
# print(solution([1, 7, 3, 21, 13, 19, 63, 1]))  # 0
# print(solution([1, 7, 15, 15, 15]))  # 3
# print(solution([1, 7, 15, 15, 15, 17]))  # 2
