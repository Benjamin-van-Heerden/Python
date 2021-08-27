def solution(data, n):
    # Your code here

    # write the counts of the numbers in data to a dictionary

    data_dict = {}

    for d in data:
        if d in data_dict:
            data_dict[d] += 1
        else:
            data_dict[d] = 1

    # mutate the data dict such that it now reports true if data_dict[i] <= n and false otherwise 
        
    data_dict = {d: val <= n for (d, val) in data_dict.items()}

    # use list comprehension to remove the numbers in data that are "falsy" in the data_dict

    result = [i for i in data if data_dict[i]]

    return result

print(solution([1, 2, 3], 0))
print(solution([1, 2, 2, 3, 3, 3, 4, 5, 5], 2))
