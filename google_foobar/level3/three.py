# restating the problem: given a single Mach and Facula bomb initially, is it possible to create the input (x, y) 
# and how many generations would it take? The structure that is generated is that of a binary tree, with root (1, 1), 
# the first leaves generated would then be something like (1, 1) -> ((2, 1), (1, 2)). What this would amount to is a sort of 
# depth first search with a pruning when the leaf node has invalid values for the mach or facula values.

class Node:
    def __init__(self, mach, facula, parent):
        self.mach = mach
        self.facula = facula
        self.parent = parent

class BombTree:
    def __init__(self):
        self.level = 0
        self.root = Node(1, 1, None)
        self.current = self.root
    
    def goto_parent(self):
        self.level -= 1
        self.current = self.current.parent

    def add_left_child(self, mach, facula):
        self.level += 1
        child = Node(mach+facula, facula, self.current)
        self.current = child

    def add_right_child(self, mach, facula):
        self.level += 1
        child = Node(mach, mach+facula, self.current)
        self.current = child
    
    def reset_root(self):
        self.level = 0
        self.current = self.root

def helper_solution(x, y, tree, root_visited=False): 
    # if the node is the solution, return the current depth of the tree.
    # if we arrive above the root node also return the depth (which will be -1) 
    if tree.current is None:
        return tree.level
    elif (tree.current.mach == x and tree.current.facula == y):
        return tree.level
    elif not root_visited:
        # the first part of the algorithm concerns itself with the left half of the tree.
        # due to the nature of the mach and facula numbers any valid combination can be found by first going diagonally
        # down left then going diagonally down right.

        # if we can still make x by combining the current mach and facula numbers create a left child (go down left)
        if (tree.current.mach + tree.current.facula) <= x:
            tree.add_left_child(tree.current.mach, tree.current.facula)
            return helper_solution(x, y, tree, root_visited)
        # if we arrive at the correct value for x going left again will fail, try going right in stead
        elif tree.current.mach == x and (tree.current.mach + tree.current.facula) <= y:
            tree.add_right_child(tree.current.mach, tree.current.facula)
            return helper_solution(x, y, tree, root_visited)
        # if neither of these are all relevant mach and facula combinations on the left half has been checked
        # we reset to the root
        else:
            tree.reset_root()
            root_visited = True
            return helper_solution(x, y, tree, root_visited)
    else:
        # we are now on the right half of the tree. much the same happens here, but we first go diagonally
        # down right then left. 

        # if we can still make y by combining the current mach and facula numbers create a right child (go down right)
        if (tree.current.mach + tree.current.facula) <= y:
            tree.add_right_child(tree.current.mach, tree.current.facula)
            return helper_solution(x, y, tree, root_visited)
        # if we arrive at the correct value for y going right again will fail, try going left in stead
        elif (tree.current.mach + tree.current.facula) <= x and tree.current.facula == y:
            tree.add_left_child(tree.current.mach, tree.current.facula)
            return helper_solution(x, y, tree, root_visited)
        # if neither of these are all relevant mach and facula combinations in the entire tree have been checked
        # we reset to the root and go to its parent so the algorithm will terminate
        else:
            tree.reset_root()
            tree.goto_parent()
            return helper_solution(x, y, tree, root_visited)

        
        

    


def solution(x, y):
    # Your code here
    bomb_tree = BombTree()
    res = helper_solution(int(x), int(y), bomb_tree)
    if res != -1:
        return str(res)
    return "impossible"


import time


print(solution('2', '5')) # 3
print(solution('2', '4')) # impossible 
print(solution('3', '2')) # 2
print(solution('4', '7')) # 4
print(solution('2', '1')) # 1
print(solution('1', '6')) # 5
print(solution('1', '1')) # 0
print(solution('3', '4')) # 3 
now = time.time()
print(solution('1', '1000')) # 999
print(f"Time: {time.time() - now}")

now = time.time()
print(solution('1', '10000')) # 9999
print(f"Time: {time.time() - now}")

now = time.time()
print(solution('1', '100000')) # 99999
print(f"Time: {time.time() - now}")

now = time.time()
print(solution('1', '10000000000000')) # 9999999999999
print(f"Time: {time.time() - now}")

now = time.time()
print(solution('100000000', '1')) # 9999999
print(f"Time: {time.time() - now}")

now = time.time()
print(solution('1234', '5555555555')) # 4502105, +/- 1.2s
print(f"Time: {time.time() - now}")

# now = time.time()
# print(solution('1234', '55555555555')) # 45020735, +/- 12s
# print(f"Time: {time.time() - now}")

# now = time.time()
# print(solution('1234', '5555555555555555')) # 45020735, +/- 12s
# print(f"Time: {time.time() - now}")

# now = time.time()
# print(solution('1234', '555555555555555555555')) # 45020735, +/- 12s
# print(f"Time: {time.time() - now}")