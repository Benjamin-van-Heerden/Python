def bin_search(list, key):
    top = len(list) - 1
    bottom = 0

    while top >= bottom:
        middle = (top + bottom)//2
        
        if list[middle] == key:
            print()
            return f"The key is at position {middle}"
        elif list[middle] >= key:
            top = middle - 1
        elif list[middle] <= key:
            bottom = middle + 1

        print(f"Currently checking position {middle}")
    
    print()

    return "Key not found"

        

print(bin_search([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 9))