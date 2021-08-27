#%%
from operator import sub
import numpy as np
import matplotlib.pyplot as plt
np.set_printoptions(precision=4)
np.set_printoptions(suppress=True)

def euclidean_distance(p, q):
    return np.linalg.norm(p-q)

def brute_force(subarray):
    delta = float("inf")
    for i in range(len(subarray)-1):
        for j in range(i+1, len(subarray)):
            actual = euclidean_distance(subarray[i], subarray[j])
            if actual < delta:
                delta = actual
    return delta

def get_strip_delta(strip_points, delta):
    strip_delta = delta
    n = len(strip_points)

    for i in range(n):
        j = i + 1
        while j < n and (strip_points[j][1] - strip_points[i][1]) < strip_delta:
            strip_delta = euclidean_distance(strip_points[j], strip_points[i])
            j = j+1
    return strip_delta


def closest_points(sorted_x, sorted_y, num_of_items):
    # when the number of points is less than 3 we use brute force
    # base case 
    if num_of_items <= 3:
        return brute_force(sorted_x)
    
    middle_index = num_of_items//2
    middle_item = sorted_x[middle_index]

    # DIVIDE PHASE
    delta_left = closest_points(sorted_x[:middle_index], sorted_y, middle_index)
    delta_right = closest_points(sorted_x[middle_index:], sorted_y, num_of_items-middle_index)

    delta = min(delta_left, delta_right)

    # CONQUER PHASE
    strip_points = sorted_y[abs(sorted_y[:, 0]-middle_item[0]) < delta]

    strip_delta = get_strip_delta(strip_points, delta)

    return min(strip_delta, delta)




# generate the points
np.random.seed(0)
points = np.random.rand(4, 2)
# sort points according to x coordinate
points_x = np.array(sorted(points, key=lambda x: x[0]))
points_y = np.array(sorted(points, key=lambda x: x[1]))

points = [
    [1, 1],
    [4, 2],
    [10, 10],
    [0, 0],
    [5, 3]
]
points_x = np.array(sorted(points, key=lambda x: x[0]))
points_y = np.array(sorted(points, key=lambda x: x[1]))

# plt.scatter(x=points[:, 0], y=points[:, 1])
# plt.show()

print(closest_points(points_x, points_y, len(points_x)))

# %%
