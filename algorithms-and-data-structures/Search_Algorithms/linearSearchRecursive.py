def linearSearchRecursiveA(container, searchValue, currentIndex=0):
    if len(container) == 0:
        return -1
    else:
        if container[0] == searchValue:
            return currentIndex
        else:
            return linearSearchRecursiveA(container[1:], searchValue, currentIndex + 1)

def linearSearchRecursiveB(container, searchValue, currentIndex=0):
    if currentIndex >= len(container):
        return -1
    else:
        if container[currentIndex] == searchValue:
            return currentIndex
        else:
            return linearSearchRecursiveB(container, searchValue, currentIndex + 1)
    


print(linearSearchRecursiveA([1, 2, 3, 4, 5, 6], 4))
print(linearSearchRecursiveA([1, 2, 3, 4, 5, 6], 8))

print(linearSearchRecursiveB([1, 2, 3, 4, 5, 6], 4))
print(linearSearchRecursiveB([1, 2, 3, 4, 5, 6], 8))