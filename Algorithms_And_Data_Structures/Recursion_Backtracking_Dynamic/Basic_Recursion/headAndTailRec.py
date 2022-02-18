def tailrec(n):
    print(f"Calling tailrec({n})")
    if n == 0: return
    else:
        print(n)
        tailrec(n-1)

def headrec(n):
    print(f"Calling headrec({n})") # twice as many operations!! 
    if n == 0: return
    else:
        headrec(n-1)
        print(n)

print("tailrec:")
print()
tailrec(5)
print()
print("headrec:")
print()
headrec(5)