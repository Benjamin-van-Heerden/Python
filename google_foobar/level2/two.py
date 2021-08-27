def helper_solution(l, accumulator):

    # base case, zero or only one element
    if len(l) == 0:
        # if there are no items left return what we have
        return accumulator
    elif len(l) == 1:
        # if there is one element include it only if it will have an effect
        if l[0] > 1:
            return accumulator*l[0]
        else:
            return accumulator
    else:
        # the approach here is to find the largest product pairs (the list is sorted)
        # since it is sorted the largest pairs can be found at the beginning and end
        # also check the pair products against the initial element
        maximal = l[0]
        prod1 = l[0]*l[1]
        prod2 = l[-1]*l[-2]

        if prod1 < 0 and prod2 < 0 and maximal < 0:
            # if all these are negative we cannot possibly increase the accumulator
            return accumulator
        elif maximal > prod1 and maximal > prod2 and maximal >= 1:
            # the maximal element has the largest effect
            return helper_solution(l[1:], accumulator*maximal)
        elif prod1 >= prod2:
            # the first two elements have the largest effect
            if prod1 <= 1:
                return accumulator
            return helper_solution(l[2:], accumulator*prod1)
        else:
            # the last two elements have the largest effect
            if prod2 <= 1:
                return accumulator
            return helper_solution(l[:-2], accumulator*prod2)


def solution(xs):
    # Your code here

    # only one panel in the array
    if len(xs) == 1:
        return str(xs[0])

    # sort the array
    xs = sorted(xs, reverse=True)

    # there is a small edge case when we have an array of zeros and a single negative e.g. [0, -1]
    # here the expected answer is 0, but the result will be 1, it is not that clean, but may be resolved
    # with an if check.

    if xs[0] == 0 and len(list(filter(lambda x: x < 0, xs))) == 1:
        return str(0)

    # if the first element is greater than zero we may trim zeros
    if xs[0] > 0:
        xs = list(filter(lambda x: x != 0, xs))

    # we instantiate the accumulator with one (it is the identity for multiplication)
    return str(helper_solution(xs, 1))



print(solution([2, 0, 2, 2, 0]))  # 8

print(solution([-2, -3, 4, -5]))  # 60

print(solution([2, -3, 1, 0, -5]))  # 30

print(solution([2]))  # 2

print(solution([-1]))  # -1

print(solution([0, -1, 0, -1]))  # 1

print(solution([1, 1, 1, -1]))  # 1

print(solution([4, 3, -1, -2, 0, 0, -4]))  # 96

print(solution([-2, -3, -4, -42, -5]))  # 2520

print(solution([0, 0, 0, -1]))  # 0

print(solution([2, -1]))  # 2
