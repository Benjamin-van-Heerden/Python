def bin_search(list, key):
    if len(list) == 0:
        return False

    middle = len(list)//2
    print(list)
    print(middle)

    if list[middle] == key:
        return True

    if list[middle] > key:
        return bin_search(list[:middle], key)
    else:
        return bin_search(list[middle+1:], key)

print(bin_search([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 8))