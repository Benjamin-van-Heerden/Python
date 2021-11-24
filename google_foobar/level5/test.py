from math import perm, comb

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

for _ in generate_subproblems(6, 4):
    print(_)