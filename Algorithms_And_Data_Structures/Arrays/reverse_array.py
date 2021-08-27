def reverse_array(arr):
    i = 0
    j = len(arr)-1
    while i < j:
        arr[i], arr[j] = arr[j], arr[i]
        i += 1
        j -= 1

l = [1, 2, 3, 4, 5, 6, 6]
reverse_array(l)
print(l)
