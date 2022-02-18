#!/usr/bin/python3

import random
from concurrent import futures
import multiprocessing

def find_items(tup):
    list, items = tup

    list.sort()
    items_found = [False]*len(items)

    for i, item in enumerate(items):
        top = len(list)-1
        bottom = 0
        while bottom <= top:
            middle = (top + bottom)//2

            if list[middle] == item:
                items_found[i] = True
                break
            if list[middle] > item:
                top = middle - 1
            if list[middle] < item:
                bottom = middle + 1

    if all(items_found):
        print(True)

    return items_found

l = random.sample(range(1, 10**10 + 1), 10**7)
items = random.sample(range(1, 10**10 + 1), 10**3)
tup = (l, items) # Takes about 10s to get to here

# print(any(find_items(tup))) # Takes about 19s real

# executor = futures.ProcessPoolExecutor() # ThreadPoolExecutor not much better (Not I/O bound) 
# future = executor.submit(find_items, tup)
# print(any(future.result()))
# executor.shutdown() # Around 19s real

# pool = multiprocessing.Pool(processes=12)
# outputs = pool.map(find_items, tup)
# print(outputs) #have to rewrite function for this implimentation to work

