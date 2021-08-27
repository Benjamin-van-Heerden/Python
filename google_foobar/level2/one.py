def dec_to_base_fill_zeros(num, base, length):
    base_num = ""
    while num>0:
        dig = int(num%base)
        base_num += str(dig)
        num //= base
    base_num = str(base_num[::-1])  #To reverse the string

    # place leading zeros if the length is less than k
    num_result = [c for c in str(base_num)]
    len_diff = length - len(num_result)
    if len_diff != 0:
        num_result = ["0"]*len_diff + num_result

    return "".join(num_result)


def next_minion_id(n, b):
    k = len(n)
    x = "".join(sorted(n, reverse=True))
    y = "".join(sorted(n))

    # convert x and y to base 10
    x_base_10 = int(x, b)
    y_base_10 = int(y, b)

    z_base_10 = x_base_10 - y_base_10

    # convert z back to base b
    z = dec_to_base_fill_zeros(z_base_10, b, k)
    return [z]

    


def contains_cycle(minions, b):
    # first determine whether a cycle exists
    m = {}
    # determine the counts of the elements -> if an element occurs twice then there must be a cycle
    # once a single element occurs three times then the cycle has restarted (and this is the root node)
    for d in minions:
        if d in m:
            m[d] += 1
        else:
            m[d] = 1

    if 2 in m.values():
        # good, we are in a cycle, now go through the next minions until a 3 is found
        while 3 not in m.values():
            minions = minions + next_minion_id(minions[-1], b)
            m = {}
            for d in minions:
                if d in m:
                    m[d] += 1
                else:
                    m[d] = 1
        
        # now the cycle has finished and restarted again
        # the length of the cycle is the number of 2's + 3's in m
        len_cycle = len(set([a for a in minions if m[a] >= 2]))
        return True, len_cycle
        

    else:
        return False, 0

def cycle_length(minions, b):
    has_cycle, cycle_len = contains_cycle(minions, b)
    if has_cycle:
        return cycle_len
    else:
        return cycle_length(minions + next_minion_id(minions[-1], b), b)


def solution(n, b):
    #Your code here
    minions = [n]
    return cycle_length(minions, b)


print(solution("1211", 10))
print(solution('210022', 3))