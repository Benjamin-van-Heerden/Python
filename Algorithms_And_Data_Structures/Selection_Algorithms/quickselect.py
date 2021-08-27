import random


class Quickselect:
    '''
    Instantiate with an unordered iterable that conforms to some topological ordering 
    (the implimentation is written with numbers in mind). Python will use its default ordering.
    Use the "run" method to return the k'th smallest item according to the ordering.
    e.g. run(1) returns the smallest item in the iterable.
    '''

    def __init__(self, nums):
        self.nums = nums

    def run(self, k):
        return self.select(0, len(self.nums)-1, k-1)

    # PARTITION PHASE
    def partition(self, first_index, last_index):
        # generate a random number in the given range
        pivot_index = random.randint(first_index, last_index)

        # swap the pivot and last_index
        self.swap(pivot_index, last_index)

        for i in range(first_index, last_index):
            # change this to > if the k'th largest item is desired
            if self.nums[i] < self.nums[last_index]:
                self.swap(first_index, i)
                first_index += 1

        # swap back such that all the items on the left are smaller and all the items on the right are larger
        self.swap(first_index, last_index)

        # return the index of the pivot item
        return first_index

    def swap(self, i, j):
        self.nums[i], self.nums[j] = self.nums[j], self.nums[i]

    # SELECTION PHASE

    def select(self, first_index, last_index, k):
        pivot_index = self.partition(first_index, last_index)

        # selection phase, compare the pivot index with k

        if pivot_index < k:
            # discard the left sub-array and keep considering the items on the right
            return self.select(pivot_index+1, last_index, k)
        elif pivot_index > k:
            # discard the right sub-array and keep considering the items on the left
            return self.select(first_index, pivot_index-1, k)
        else:
            # we have found the item we are looking for
            return self.nums[pivot_index]


l = [1, 2, 3, 4, 5, 67, 21, 32, -5, -42]

select = Quickselect(l)

# smallest item
print(select.run(1))
