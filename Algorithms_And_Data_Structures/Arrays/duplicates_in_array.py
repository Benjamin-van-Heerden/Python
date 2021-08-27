def duplicates(arr):
    arr_items = {}

    for item in arr:
        if item in arr_items:
            return True
        else:
            arr_items[item] = 1
    
    return False

# this is again O(N), (but also O(N) in space), if we we do not use additional memory we can achieve O(NlogN)
# since we would have to sort the array

print(duplicates([1, 2, 3, 4]))
print(duplicates([1, 2, 3, 4, 1]))

# if there is an additional restriction that the items in the array do not exceed the length of the array
# we can achieve O(N) in-place, zero also not included
print()

def another_duplicates(arr):
    for i in range(len(arr)):
        if arr[abs(arr[i]-1)] > 0:
            # flip the sign
            arr[abs(arr[i]-1)] *= -1
        else:
            # if we have a negative it must be a repetition
            # print(i)
            return True
    return False

# this is O(N), but not very practical
print(another_duplicates([1, 2, 3, 4]))
print(another_duplicates([1, 2, 3, 4, 1]))