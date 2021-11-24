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
# to maximise the number of games that cycle such that the most possible trainers are distracted. One approach is
# to convert the graph into a flow network and calculate the maximum flow through the bipartite network

from fractions import gcd


def game_will_cycle(m, n):
    num = (m + n) // gcd(m, n)
    return not (num & -num) == num


def solution(banana_list):
    # require at least two trainers for games to be played
    if len(banana_list) == 1:
        return 1
    # we convert the games that will cycle to a flow network. this entails converting the graph to a directed graph
    # and adding a source and a sink. the graph will have |V| = 2 * (len(banana_list) + 1) and edges where there are
    # cyclic games. since len(banana_list) <= 100 and there may be up to 10 000 edges an algorithm that places less
    # emphasis on the number of edges is preferred.

    # the source is connected to all vertices on the left set
    source_vertex = [0] + [1] * len(banana_list) + [0] * (len(banana_list) + 1)

    # the sink has no outgoing edges
    sink_vertex = [0] * (2 * len(banana_list) + 2)

    left_vertices = []
    unique_edges = {}
    for i in range(len(banana_list)):
        # the left vertices are not connected to themselves or the source. we also only consider the unique edges
        # part for each of the vertices in the left set. this is because we do not want duplicate matches. e.g.
        # if vertex 0 has a cyclic game with vertex 4 then by symmetry vertex 4 also has a cyclic game with vertex 0
        # both of these represent the same game so we only take one of them
        current = [0] * (len(banana_list) + 1)
        for j in range(len(banana_list)):  # this is the "upper triangular part"
            if game_will_cycle(banana_list[i], banana_list[j]):
                if (i, j) in unique_edges or (j, i) in unique_edges:
                    current.append(0)
                else:
                    current.append(1)
                    unique_edges[(i, j)] = True
                    unique_edges[(j, i)] = True
            else:
                current.append(0)
        # they are also not connected to the sink
        current += [0]
        left_vertices.append(current)

    right_vertices = []
    for i in range(len(banana_list)):
        # the right vertices are connected to nothing other than the sink
        right_vertices.append([0] * (2 * len(banana_list) + 1) + [1])

    flow_network = [source_vertex, *left_vertices, *right_vertices, sink_vertex]

    print(flow_network)

    return len(banana_list) - ford_fulkerson(flow_network, 0, len(flow_network) - 1)


def ford_fulkerson(flow_graph, source, sink):
    # this array is filled by bfs
    parent = [-1] * (len(flow_graph))
    # initially there is no flow through the network
    max_flow = 0

    # while there is a valid path from the source to the sink we augment the flow
    while bfs(source, sink, parent, flow_graph):
        # a path is found so we find the maximum flow through this path
        path_flow = float("Inf")
        s = sink
        while s != source:
            path_flow = min(path_flow, flow_graph[parent[s]][s])
            s = parent[s]

        # additional flow is available, add the path flow to the current max_flow
        max_flow += path_flow

        # update residual capacities of the edges and reverse edges along the path
        v = sink
        while v != source:
            u = parent[v]
            flow_graph[u][v] -= path_flow
            flow_graph[v][u] += path_flow
            v = parent[v]

    return max_flow


def bfs(s, t, parent, flow_graph_bfs):
    # initially all vertices are unvisited
    visited = [False] * len(flow_graph_bfs)
    # bfs will be handled using a queue like structure, initialize it.
    # the first vertex we visit is the source. mark it as visited and enqueue it
    queue = [s]
    visited[s] = True

    # bfs loop
    while queue:
        # dequeue a vertex for bfs
        u = queue.pop(0)

        # now we loop. we get all connected vertices of the dequeued vertex u. if a connected vertex has not been
        # visited, mark it as such and enqueue it
        for i, val in enumerate(flow_graph_bfs[u]):
            if not visited[i] and val > 0:
                # the bfs terminates when we hit the sink node. we set its parent and we return True
                queue.append(i)
                visited[i] = True
                parent[i] = u
                if i == t:
                    return True
    # the sink could not be reached so we return false
    return False



# print(solution([300]))  # 1
# print(solution([1, 1]))  # 2
# print(solution([1, 7, 3, 21, 13, 19]))  # 0
# print(solution([1, 3, 7, 15]))  # 2
# print(solution([13, 3]))  # 2
print(solution([5, 2, 3]))  # 1
# print(solution([3, 5]))  # 2
#
# print(solution([1073741823, 1]))  # 2
# print(solution([1073741823, 2]))  # 0
# print(solution([1, 7, 3, 21, 13, 19, 6, 18, 42]))  # 1
# print(solution([1, 7, 3, 21, 13, 19, 6, 18]))  # 0
# print(solution([1, 7, 3, 21, 13, 19, 63, 1]))  # 0
# print(solution([1, 7, 15, 15, 15]))  # 3
# print(solution([1, 7, 15, 15, 15, 17]))  # 2
