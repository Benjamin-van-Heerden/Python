def binary(container, value, left, right):
    if right < left:
        return -1
    else:
        middleIndex = (left + right)//2
        if container[middleIndex] == value:
            return middleIndex
        else:
            if value > container[middleIndex]:
                print("Checking items on the right")
                return binary(container, value, middleIndex+1, right)
            else:
                print("Checking items on the left")
                return binary(container, value, left, middleIndex-1)




    


l = [-42, -32, -5, -2, 5, 42, 62, 66, 75, 89, 102, 540, 1002, 3600, 7654]

print(binary(l,-2, 0, len(l)))
print(binary(l, -42, 0, len(l)))
print(binary(l, -5, 0, len(l)))
print(binary(l, 540, 0, len(l)))
print(binary(l, 7654, 0, len(l)))

print(binary(l, 1, 0, len(l)))