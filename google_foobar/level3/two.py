import time
from functools import reduce

def xor_checksum(packet):
    checksum = 0
    
    for el in packet:
        checksum ^= el
    
    return checksum

def solution(start, length):
    # Your code here

    # the implimentation I have settled on relies on modulo operations and it is O(N)
    # the idea is to start the modulus at the length of the workers' queue and decrement it when a new queue has formed
    # this happens when (worker_id - start) % length == 0 (taking care to exclude the first occurrence)

    packet = []

    modulus = length
    mod_counter = 0

    # start from zero such that taking the modulo makes sense
    index = 0
    now = time.time()
    while modulus >= 0:
        # if the (index % length) == 0 this means that a new queue has formed
        if index % length == 0:
            mod_counter += 1
            if mod_counter == 2:
                modulus -= 1
                # reinitialise to 1 as to not skip the current index
                mod_counter = 1
        
        if mod_counter <= 1 and index % length < modulus:
            # add the index + start such that we have the correct worker id's
            packet.append(index+start)
        
        index += 1    

    print(f"Time Packet = {time.time() - now}")

    now = time.time()
    result = int(xor_checksum(packet))
    print(f"Time XOR = {time.time() - now}")

    return result


# print(solution(0, 3)) # 2
# print(solution(17, 4)) # 14

# print(solution(12, 5)) # 42

# print(solution(0, 1))

print(solution(1000000000, 1000))
