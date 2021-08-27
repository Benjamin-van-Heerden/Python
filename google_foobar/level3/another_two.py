# import time

def solution(start, length):
    # Your code here

    # we must first establish how far to go. The worker queues always have fixed length (the first worker is included)
    
    end_worker_id = start + length*length - 1

    # the implimentation I have settled on will add items on a take then skip basis
    # the xor operation will be done while the loop is running

    result = 0

    # the take is equal to the length and the skip is equal to zero. take and skip always sum to length
    take = length
    skip = 0
    index = start

    # now = time.time()

    while index <= end_worker_id:
        if take > 0:
            for i in range(index, index + take):
                result ^= i
            index += take 
            take = 0
        else:
            index += skip
            skip += 1
            take = length - skip
        
    # print(f"Time Packet = {time.time() - now}")

    return result


print(solution(0, 3)) # 2
print(solution(17, 4)) # 14

print(solution(12, 5)) # 42

print(solution(0, 1)) # 0

print(solution(101, 1)) # 101

print(solution(1000000000, 1000)) # 528128

print(solution(1000000000, 10000)) # 2080235520