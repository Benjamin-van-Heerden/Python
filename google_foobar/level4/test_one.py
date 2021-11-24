import math

def gen_valid_points_length(your_position, trainer_position, dimensions, distance):
    reflected_replicates_trainer = [trainer_position]
    reflected_replicates_your = [your_position]
    # hlines and vlines are just for visualization purposes
    hlines = [0]
    vlines = [0]

    (
        additional_upward_your_points,
        additional_upward_trainer_points,
        additional_upward_hlines,
        additional_upward_vlines,
    ) = propagate_vertically(
        dimensions[0],
        dimensions[1],
        your_position,
        trainer_position,
        distance,
        upwards=True,
    )

    (
        additional_downward_your_points,
        additional_downward_trainer_points,
        additional_downward_hlines,
        additional_downward_vlines,
    ) = propagate_vertically(
        dimensions[0],
        dimensions[1],
        your_position,
        trainer_position,
        distance,
        upwards=False,
    )

    reflected_replicates_trainer += (
        additional_upward_trainer_points + additional_downward_trainer_points
    )
    reflected_replicates_your += (
        additional_upward_your_points + additional_downward_your_points
    )

    hlines += additional_upward_hlines + additional_downward_hlines
    vlines += additional_upward_vlines + additional_downward_vlines

    hlines = list(set(hlines))
    vlines = list(set(vlines))

    # now that we have the possible paths that will lead to hits on the trainer we need to remove
    # invalid paths

    # first we convert the valid trainer- and your points to directional vectors eminating from your_position
    # in the base cell

    reflected_replicates_trainer = list(
        map(
            lambda x: to_directional_vect(your_position, x),
            reflected_replicates_trainer,
        )
    )
    reflected_replicates_your = list(
        map(lambda x: to_directional_vect(your_position, x), reflected_replicates_your)
    )

    # first we remove all paths that would hit your position (i.e. all paths hitting an instance of a
    # reflected your position before hitting the reflected trainer position)

    trainers_remove = []

    for i in range(len(reflected_replicates_trainer)):
        for j in range(len(reflected_replicates_your)):
            trainer_x, trainer_y = (
                reflected_replicates_trainer[i][0],
                reflected_replicates_trainer[i][1],
            )
            your_x, your_y = (
                reflected_replicates_your[j][0],
                reflected_replicates_your[j][1],
            )

            if trainer_x == -3 and trainer_y == 0:
                print("now")

            # if the your directional vector is a scalar multiple of the trainer directional vector and the scalar is < 1 it must be removed
            # if either of the denominators are zero we have special cases (both cannot be zero at the same time):
            if your_x == 0 and your_y == 0:
                # when we hit the base cell
                pass
            elif trainer_x == 0 and your_x != 0:
                continue
            elif trainer_y == 0 and your_y != 0:
                continue
            elif trainer_x == 0 and your_x == 0:
                if abs(your_y) < abs(trainer_y) and your_y * trainer_y > 0:
                    trainers_remove.append(reflected_replicates_trainer[i])
            elif trainer_y == 0 and your_y == 0:
                if abs(your_x) < abs(trainer_x) and your_x * trainer_x > 0:
                    trainers_remove.append(reflected_replicates_trainer[i])
            else:
                d1 = your_x / trainer_x
                d2 = your_y / trainer_y
                if d1 == d2 and d1 < 1:
                    trainers_remove.append(reflected_replicates_trainer[i])

    # convert to sets of tuples such that set operations are available
    reflected_replicates_trainer = set([tuple(v) for v in reflected_replicates_trainer])
    trainers_remove = set([tuple(v) for v in trainers_remove])

    reflected_replicates_trainer = reflected_replicates_trainer.difference(
        trainers_remove
    )

    # # finally we remove all duplicate paths (paths first hitting a reflected trainer position before then
    # # moving on and hitting another trainer position)
    # # the easiest way I can think of doing this is first converting them to a list of unit vectors, then to a set

    reflected_replicates_trainer = [list(t) for t in list(reflected_replicates_trainer)]
    reflected_replicates_trainer = list(map(lambda x: to_unit(x), reflected_replicates_trainer))
    reflected_replicates_trainer = set([tuple(v) for v in reflected_replicates_trainer])

    return len(reflected_replicates_trainer)


def to_unit(vector):
    mag = math.sqrt(sum([v ** 2 for v in vector]))
    return [round(v / mag, 8) for v in vector]


def to_directional_vect(from_vect, to_vect):
    return [to_vect[0] - from_vect[0], to_vect[1] - from_vect[1]]


def propagate_vertically(
    x_dim, y_dim, your_pos, trainer_pos, max_distance, upwards=True
):
    # this function checks where there are allowed trainer points, propagating vertically
    # subject to the constraint that the distance to the next trainer point is <= max_distance

    your_distance_from_top = y_dim - your_pos[1]
    your_distance_from_bottom = your_pos[1]
    trainer_distance_from_top = y_dim - trainer_pos[1]
    trainer_distance_from_bottom = trainer_pos[1]
    additional_vertical_trainer_points = []
    additional_vertical_your_points = []
    additional_hlines = []
    additional_vlines = []

    # as a first step, propagate horizontally in bouth directions from the base cell (no need to do twice)
    if upwards:
        (
            additional_rightward_your_points,
            additional_rightward_trainer_points,
            additional_rightward_vlines,
        ) = propagate_horizontally(
            x_dim,
            your_pos,
            your_pos,
            trainer_pos,
            max_distance,
            additional_vlines,
            right=True,
        )

        (
            additional_leftward_your_points,
            additional_leftward_trainer_points,
            additional_leftward_vlines,
        ) = propagate_horizontally(
            x_dim,
            your_pos,
            your_pos,
            trainer_pos,
            max_distance,
            additional_vlines,
            right=False,
        )

        additional_vertical_your_points += (
            additional_rightward_your_points + additional_leftward_your_points
        )
        additional_vertical_trainer_points += (
            additional_rightward_trainer_points + additional_leftward_trainer_points
        )

        additional_vlines += additional_rightward_vlines + additional_leftward_vlines

    # now we propagate vertically either up or down and while we visit the new reflections
    # propagate left and right as well
    if upwards:
        i = 1
    else:
        i = -1
    sign = 1
    trainer_x = trainer_pos[0]
    your_x = your_pos[0]
    while True:
        if sign == 1:
            trainer_new_y = i * y_dim + trainer_distance_from_top
            your_new_y = i * y_dim + your_distance_from_top
        else:
            trainer_new_y = i * y_dim + trainer_distance_from_bottom
            your_new_y = i * y_dim + your_distance_from_bottom

        dist = math.dist(your_pos, [trainer_x, trainer_new_y])

        if dist <= max_distance:
            additional_vertical_trainer_points.append([trainer_x, trainer_new_y])
            additional_vertical_your_points.append([your_x, your_new_y])
            additional_hlines.append(i * y_dim)

            # while we are here we might as well propagate horizontally using [trainer_x, trainer_new_y]
            # and [your_x, your_new_y]
            (
                additional_rightward_your_points,
                additional_rightward_trainer_points,
                additional_rightward_vlines,
            ) = propagate_horizontally(
                x_dim,
                your_pos,
                [your_x, your_new_y],
                [trainer_x, trainer_new_y],
                max_distance,
                additional_vlines,
                right=True,
            )

            (
                additional_leftward_your_points,
                additional_leftward_trainer_points,
                additional_leftward_vlines,
            ) = propagate_horizontally(
                x_dim,
                your_pos,
                [your_x, your_new_y],
                [trainer_x, trainer_new_y],
                max_distance,
                additional_vlines,
                right=False,
            )

            additional_vertical_your_points += (
                additional_rightward_your_points + additional_leftward_your_points
            )
            additional_vertical_trainer_points += (
                additional_rightward_trainer_points + additional_leftward_trainer_points
            )

            additional_vlines += (
                additional_rightward_vlines + additional_leftward_vlines
            )
            ########################
            sign *= -1
            if upwards:
                i += 1
            else:
                i -= 1
        else:
            if upwards:
                additional_hlines.append(i * y_dim)
            break
    return (
        additional_vertical_your_points,
        additional_vertical_trainer_points,
        additional_hlines,
        additional_vlines,
    )


def propagate_horizontally(
    x_dim,
    original_your_pos,
    your_pos,
    trainer_pos,
    max_distance,
    additional_vlines,
    right=True,
):
    # this function is very similar to the vertical propagation, the additional parameter "original_your_pos"
    # controls the allowed (subject to the distance) trainer points in ther vertical direction

    your_distance_from_right = x_dim - your_pos[0]
    your_distance_from_left = your_pos[0]
    trainer_distance_from_right = x_dim - trainer_pos[0]
    trainer_distance_from_left = trainer_pos[0]
    additional_horizontal_trainer_points = []
    additional_horizontal_your_points = []
    additional_vlines = []

    if right:
        i = 1
    else:
        i = -1
    sign = 1
    trainer_y = trainer_pos[1]
    your_y = your_pos[1]
    while True:
        if sign == 1:
            trainer_new_x = i * x_dim + trainer_distance_from_right
            your_new_x = i * x_dim + your_distance_from_right
        else:
            trainer_new_x = i * x_dim + trainer_distance_from_left
            your_new_x = i * x_dim + your_distance_from_left

        dist = math.dist(original_your_pos, [trainer_new_x, trainer_y])

        if dist <= max_distance:
            additional_horizontal_trainer_points.append([trainer_new_x, trainer_y])
            additional_horizontal_your_points.append([your_new_x, your_y])
            additional_vlines.append(i * x_dim)
            sign *= -1
            if right:
                i += 1
            else:
                i -= 1
        else:
            if right:
                additional_vlines.append(i * x_dim)
            break
    return (
        additional_horizontal_your_points,
        additional_horizontal_trainer_points,
        additional_vlines,
    )


import matplotlib.pyplot as plt
import seaborn as sns

sns.set_style("darkgrid")

dimensions = [3, 2]
your_position = [1, 1]
trainer_position = [2, 1]
distance = 4

dimensions = [300,275]
your_position = [150,150]
trainer_position = [185,100]
distance = 500

trainer, your, hlines, vlines = gen_points(
    your_position, trainer_position, dimensions, distance
)


for i in range(len(trainer)):
    plt.plot(*trainer[i], "rx")

for i in range(len(your)):
    plt.plot(*your[i], "bo")

for h in hlines:
    plt.axhline(h, c="black")

for v in vlines:
    plt.axvline(v, c="black")


plt.show()
