# this solution relies heavily on the polya-redfield enumeration theorem. I found this theorem by asking for help on
# stack exchange and to be honest, much of the theorem itself is beyond my understanding.
# to approach this problem we start by looking into the mathematics of groups. we consider two configurations, A and B
# to be equivalent when B can be obtained from A via one or more row and column swaps. our task is then to find the
# number of base configurations for an input (w, h, s), from which every other configuration can be obtained via one or
# more row or column swaps.

def factorial_table(n):
    """
    builds up the table of required factorials

    :param n: factorials up to n
    :return: list of factorials up to n
    """
    factorials = [1]
    for i in range(2, n + 1):
        factorials.append(factorials[-1] * i)
    return factorials


def factorial(i, f_table):
    """
    read the factorial from the precomputed table

    :param i: positive integer
    :param f_table: previously computed factorial table
    :return: the factorial of i
    """
    return f_table[i - 1]


def gcd_table(n):
    """
    builds a table of gcd's for all (i, j) with i, j <= n

    :param n:
    :return: table of gcd's
    """
    table = [[0 for _ in range(n)] for __ in range(n)]

    for i in range(n):
        for j in range(i, n):
            if i == 0 or j == 0:
                table[i][j] = 1
                table[j][i] = 1
            elif i == j:
                table[i][j] = i + 1
            else:
                table[i][j] = table[i][j - i - 1]
                table[j][i] = table[i][j - i - 1]
    return table


def gcd(i, j, g_table):
    """
    :param i: positive integer
    :param j: positive integer
    :param g_table: previously computed table of gcd's
    :return: gcd(i, j)
    """
    return g_table[i - 1][j - 1]


def find_partition_ways(p, n, f_table):
    """
    this function computes the number:
        n!/(1^{i_1}i_1!2^{i_2}i_2!...n^{i_n}i_n!)
    where p is an integer partition of n that has i_1 1s, i_2 2s, ..., and i_n ns.
    this number is described in https://franklinvp.github.io/2020-06-05-PolyaFooBar/.
    it is a measure of how many ways the partition can be made up with given parameters

    :param p: integer partition as a list
    :param n: integer
    :param f_table: previously computed factorial table
    :return: the described number
    """
    counts = {}
    for counter in p:
        if counter in counts:
            counts[counter] += 1
        else:
            counts[counter] = 1
    result = factorial(n, f_table)
    for color, frequency in counts.items():
        result //= (color ** frequency) * factorial(frequency, f_table)
    return result


def partitions_and_ways(total_nodes, f_table):
    """
    iterative algorithm to compute all the integer partitions of a given number as well as the "ways" they may
    be formed from the function find_partition_ways(p, n, f_table). the algorithm itself can be found in this paper
    https://arxiv.org/pdf/0909.2331.pdf, as discussed in the docstring of solution(w, h, s).

    :param total_nodes: integer
    :param f_table: previously computed factorial table
    :return: a list of tuples of the partitions and their "ways"
    """
    k = 0  # index of last element in a partition
    p = total_nodes * [0]  # to store a partition in p[0:k+1]
    p[0] = total_nodes  # first partition is [n]

    # the loop stops when the current partition has all 1s
    temp_all_partitions = [0 for i in range(total_nodes + 1)]
    k = 1
    y = total_nodes - 1
    result = []  # to store all the partitions
    while k != 0:
        x = temp_all_partitions[k - 1] + 1
        k -= 1
        while 2 * x <= y:
            temp_all_partitions[k] = x
            y -= x
            k += 1
        while x <= y:
            temp_all_partitions[k] = x
            temp_all_partitions[k + 1] = y
            partition = temp_all_partitions[:k + 2]
            result.append((partition, find_partition_ways(partition, total_nodes, f_table)))
            x += 1
            y -= 1
        temp_all_partitions[k] = x + y
        y = x + y - 1
        partition = temp_all_partitions[:k + 1]
        result.append((partition, find_partition_ways(partition, total_nodes, f_table)))
    return result


def solution(w, h, s):
    """
    for positive integers w, h, s consider the equivalence classes of w x h matrices, with entries on the set
    S = {1, 2, ..., s}, identified by arbitrary permutations of the rows and the columns.
    The goal is to compute the number of those classes.

    we consider the group G = S_w x S_h, where S_w and S_h are the symmetric groups of the sets W = {1, 2, ..., w} and
    H = {1, 2, ..., h}. the group G acts on the set X = W x H, which is viewed as the set of indices of the entries of
    the matrices.
    each matrix is a function f: X -> S and f is an element of S^X.

    the problem is then to calculate the cardinality: |S^X /G|.

    polya's enumeration theorem solves this for us by counting the number of orbits under G. specifically, we employ a
    generating function called the cycle index and set the weights of the s "colors" equal to zero, we do this since
    the colors are interchangeable and carry equal importance.
    this link: https://franklinvp.github.io/2020-06-05-PolyaFooBar/, identifies the problem and poses its solution.

    these wikipedia articles were also helpful in understanding the problem and its solution:
    - https://en.wikipedia.org/wiki/Permutation_group
    - https://en.wikipedia.org/wiki/P%C3%B3lya_enumeration_theorem
    - https://en.wikipedia.org/wiki/Direct_product_of_groups#:%7E:text=In%20mathematics%2C%20specifically%20in%20group,of%20direct%20product%20in%20mathematics.
    - https://en.wikipedia.org/wiki/Symmetric_group

    once we know the formula for the solution, the main implementation challenges are to find:
    - the integer partitions of a number. I found an efficient algorithm here: https://arxiv.org/pdf/0909.2331.pdf
    - the greatest common divisors of many numbers. for this one could use the euclidean algorithm, which is very
    efficient in calculating the gcd of two numbers, but since we will need the gcd's of many numbers, it will be even
    more efficient to precalculate the a full table of the gcd's by using dynamic programming. specifically,
    if a > b, then gcd(a, b) = gcd(a - b, b). this recurrence relation allows us to compute gcd of larger pairs
    of numbers in terms of smaller pairs. in the table, one has the initial values gcd(1, a) = gcd(a, 1) = 1 and
    gcd(a, a) = a, for all a.
    - the factorials of many numbers. here again it is better to calculate all the needed factorials beforehand.

    :param w: width of the matrix
    :param h: height of the matrix
    :param s: number of colors to consider
    :return: the cardinality: |S^X /G|
    """

    # compute the gcd and factorial tables (up to max(w, h)):
    n = max(w, h)
    f_table = factorial_table(n)
    g_table = gcd_table(n)

    # use the formula to calculate the result
    result = 0
    for w_cycle in partitions_and_ways(w, f_table):
        for h_cycle in partitions_and_ways(h, f_table):
            m = w_cycle[1] * h_cycle[1]
            result += m * (s ** sum([sum([gcd(i, j, g_table) for i in w_cycle[0]]) for j in h_cycle[0]]))

    return str(result // (factorial(w, f_table) * factorial(h, f_table)))


print(solution(2, 3, 4))
print(solution(12, 12, 20))
