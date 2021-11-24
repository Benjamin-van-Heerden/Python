from functools import reduce
from math import factorial, perm, pow, comb


def find_cardinality(partition, num_colors):
    full_length = len(partition)
    truncated_length = len(set(partition))
    if full_length == truncated_length:
        return perm(num_colors, full_length)
    else:
        counts = {}
        for n in partition:
            if n in counts:
                counts[n] += 1
            else:
                counts[n] = 1

        temp_total = num_colors
        result = 1
        for val in counts.values():
            result *= comb(temp_total, val)
            temp_total -= val
        return result


# first we have to generate all the integer partitions of
# using a modified version of the ruleAsc algorithm (see: https://jeromekelleher.net/category/combinatorics.html)
def generate_subproblems(total_nodes, colors):
    all_partitions = [0 for i in range(colors)]
    k = 1
    all_partitions[0] = 0
    all_partitions[1] = total_nodes
    while k != 0:
        x = all_partitions[k - 1] + 1
        y = all_partitions[k] - 1
        k -= 1
        while x <= y and k < colors - 1:
            all_partitions[k] = x
            y -= x
            k += 1
        all_partitions[k] = x + y

        current_partition = all_partitions[:k + 1]
        cardinality = find_cardinality(current_partition, colors)
        yield current_partition, cardinality


#
# def accel_asc(n, c):
#     a = [0 for i in range(c)]
#     k = 1
#     y = n
#     while k != 0:
#         x = a[k - 1] + 1
#         k -= 1
#         while 2 * x <= y and k < c - 1:
#             a[k] = x
#             y -= x
#             k += 1
#         while x <= y:
#             a[k-1] = x
#             a[k] = y
#             yield a[:k]
#             x += 1
#             y -= 1
#         a[k] = x + y
#         y = x + y - 1
#         yield a[:k + 1]


def check_working_configurations(configuration, cardinality):
    total = sum(configuration)
    factorials = [factorial(c) for c in configuration]
    denom = 1
    for r in factorials:
        denom *= r
    return cardinality * (factorial(total) / denom)


def solution(w, h, s):
    gen = generate_subproblems(w * h, s)
    total_configs = 0
    for (configuration, cardinality) in gen:
        # total_configs += check_working_configurations(configuration, cardinality)
        print(configuration, cardinality)
        pass

    return str(f"{total_configs:.2f}")


# lowes_sol = 100000000000000000000000000000000000
# m_n_s = (0, 0, 0)
# for m in range(1, 6):
#     for n in range(1, 6):
#         for s in range(1, 8):
#             sol = solution(m, n, s)
#             if sol != 0:
#                 if abs(sol) < lowes_sol:
#                     lowes_sol = sol
#                     m_n_s = (m, n, s)
#                     print(lowes_sol)
#
# print(m_n_s)

print(solution(2, 3, 3))


def accel_asc(n, c):
    a = [0 for i in range(c + 1)]
    k = 1
    y = n
    while k != 0:
        x = a[k - 1] + 1
        k -= 1
        while 2 * x <= y - 2 and k < c - 1:
            a[k] = x
            y -= x
            k += 1
        while x <= y:
            a[k-1] = x
            a[k] = y
            yield a[:k]
            x += 1
            y -= 1
        a[k] = x + y
        y = x + y - 1
        yield a[:k + 1]


# for _ in accel_asc(6, 3):
#     print(_)
