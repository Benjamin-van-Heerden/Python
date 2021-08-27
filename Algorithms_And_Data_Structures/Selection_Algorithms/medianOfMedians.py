
def median_algorithm(nums, k):
    '''
    k is the k'th order statistic (smallest)
    Calculate the median of medians, use it as the pivot, generating the left and right
    sub arrays via list comprehension. Discard the unused sub array and repeat the process
    until the correct pivot value is achieved. 
    '''

    # split the array into chunks of 5 items

    chunks = [nums[i:i+5] for i in range(0, len(nums), 5)]

    # sort the chunks use e.g. insertion sort

    medians = [sorted(chunk)[len(chunk)//2] for chunk in chunks]

    # use the median of medians as our pivot value
    # this is approximately the median of the entire array

    pivot_value = sorted(medians)[len(medians)//2]


    # partition via list comprehension
    left_array = [n for n in nums if n < pivot_value]
    right_array = [n for n in nums if n > pivot_value]

    pivot_index = len(left_array)

    if k-1 < pivot_index:
        return median_algorithm(left_array, k)
    elif k-1 > pivot_index:
        return median_algorithm(right_array, k-pivot_index-1)

    return pivot_value   

l = [-2, -55, -42, 12, 2, 3, 4, 5, 87, 102, 42, 36, 72, -100]

for i in range(len(l)):
    print(f"k={i+1} smallest: {median_algorithm(l, i+1)}")

print(sorted(l))