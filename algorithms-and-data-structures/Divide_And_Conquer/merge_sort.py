def merge_sort(l):
    if len(l) == 1:
        return
    else:
        left = l[:len(l)//2]
        right = l[len(l)//2:]

        merge_sort(left)
        merge_sort(right)

        i = 0
        j = 0
        k = 0
        while i < len(left) and j < len(right):
            if left[i] > right[j]:
                l[k] = left[i]
                i += 1
            else:
                l[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            l[k] = left[i]
            i += 1
            k += 1
        
        while j < len(right):
            l[k] = right[j]
            j += 1
            k += 1
        

l = [3, 5, 6, 10, 1, 4, 8]

merge_sort(l)
print(l)