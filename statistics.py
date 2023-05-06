import math

import matplotlib.pyplot as plt


def calc_dist(coordinate):
    return math.sqrt(coordinate[0] ** 2 + coordinate[1] ** 2)

def draw_distrabution(list_of_blocks, resolution):
    max_distance = 0
    for block in list_of_blocks:
        if calc_dist(block) > max_distance:
            max_distance = calc_dist(block)
    bucket_diff = max_distance / (resolution - 1)
    result = [0] * resolution
    for block in list_of_blocks:
        result[round(calc_dist(block) / bucket_diff)] += 1
    plt.plot(result)
    plt.show()
    return result

def draw_scene(asda, drones, list_of_blocks):

