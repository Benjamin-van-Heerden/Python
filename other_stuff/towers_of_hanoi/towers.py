class Disk:
    def __init__(self, current_pole_position, radius):
        self.current_pole_position = current_pole_position
        self.radius = radius


def towers_of_hanoi(n):
    if n == 1:
        return 1
    else:
        return 2 * towers_of_hanoi(n - 1) + 1


def triangular_numbers_one_past(n):
    tri = [1]
    i = 0
    while True:
        t = tri[i] + (i + 2)
        if t < n + (i + 2):
            tri.append(t)
            i += 1
        else:
            break
    return tri

def towers_of_hanoi_44(n):
    if n == 1:
        return 1
    elif n == 2:
        return 3
    else:
        return 2 * towers_of_hanoi(n - 1) + 1

def towers_of_hanoi_4(n):
    if n == 1:
        return 1
    elif n == 2:
        return 3
    else:
        triangles1 = triangular_numbers_one_past(n)
        triangles2 = triangular_numbers_one_past(n + 1)
        if triangles1[-1] != triangles2[-1]:
            stacks = [i for i in range(1, len(triangles1) + 1)]
        else:
            print(triangles2)
            diff = triangles2[-1] - n
            print(diff)
            stacks = [i for i in range(1, len(triangles2))]
        return stacks


print(triangular_numbers_one_past(7))
print([towers_of_hanoi(i + 1) for i in range(5)])
print(towers_of_hanoi_4(7))

