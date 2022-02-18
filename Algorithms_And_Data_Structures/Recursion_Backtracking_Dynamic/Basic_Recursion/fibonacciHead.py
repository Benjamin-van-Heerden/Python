def fibHead(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibHead(n - 1) + fibHead(n - 2)

print(fibHead(37)) # Very inefficient!!