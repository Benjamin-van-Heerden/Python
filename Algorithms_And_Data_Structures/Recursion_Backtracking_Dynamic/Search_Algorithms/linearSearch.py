def linearSearch(container, searchValue):
    for (index, item) in enumerate(container):
        if item == searchValue:
            return index
    return -1

print(linearSearch([1, 2, 3, 4, 5, 6], 4))
print(linearSearch([1, 2, 3, 4, 5, 6], 8))