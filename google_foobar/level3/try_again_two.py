# the poblem we face with this challenge is that the array of worker queues generated is of dimension (length x length)
# suppose we put result = 0 and traverse the worker queue, XOR'ing the result with every relevant worker in the queue
# what we would end up with is an algorith of O(N^2), which is not practical. we need to traverse the worker queue in some way at least
# once. Time can thereby be saved with the XOR operation. Fortunately, there exists a way to XOR consecutive numbers in O(1), leading
# to a final algorithm of O(N). 

def xor_from_one(n):
    mod = n % 4
    if mod == 0:
        return n
    elif mod == 1:
        return 1
    elif mod == 2:
        return n + 1
    else:
        return 0

def xor_in_range(start, end):
    return xor_from_one(start-1)^xor_from_one(end)


def solution(start, length):
    # Your code here

    # we initialise a take variable to the length of the queue (-1 since it is zero indexed), which will be decremented as we traverse the queues
    # also initialise the result
    result = 0
    take = length-1
    for i in range(length):
        current_employee_id = start + i*length
        result ^= xor_in_range(current_employee_id, current_employee_id+take)
        take -= 1
    return result


import time

print(solution(0, 3)) # 2
print(solution(17, 4)) # 14

print(solution(12, 5)) # 42

print(solution(0, 1)) # 0

print(solution(101, 1)) # 101

now = time.time()
print(solution(1000000000, 1000)) # 528128
print(f"Time: {time.time() - now}")

now = time.time()
print(solution(1000000000, 10000)) # 2080235520
print(f"Time: {time.time() - now}")

now = time.time()
print(solution(1000000000, 100000))
print(f"Time: {time.time() - now}")

now = time.time()
print(solution(1000000000, 1000000))
print(f"Time: {time.time() - now}")

now = time.time()
print(solution(1000000000, 10000000))
print(f"Time: {time.time() - now}")