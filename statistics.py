import math

import matplotlib.pyplot as plt
from matplotlib.patches import Circle


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
    print(result[0])
    print(result[0]/1000)
    plt.plot(result)
    plt.show()
    return result

def draw_scene(asda, list_of_blocks):
    asda_kill_drawing = Circle((0, 0), asda._r_loss, color='red', fill=False)
    asda_safe_drawing = Circle((0, 0), asda.r_safe, color='green', fill=False)
    # plt.margins(1, 1)
    plt.gca().add_patch(asda_kill_drawing)
    plt.gca().add_patch(asda_safe_drawing)
    for drone in asda._drones:
        drone_drawing = Circle((drone.x, drone.y), drone.radius, color='blue', fill=False)
        plt.gca().add_patch(drone_drawing)
    list_of_blocks_x = []
    list_of_blocks_y = []
    for i in range(len(list_of_blocks)):
        list_of_blocks_x.append(list_of_blocks[i][0])
        list_of_blocks_y.append(list_of_blocks[i][1])
    plt.scatter(list_of_blocks_x, list_of_blocks_y, color='green')
    # for i in range(len(list_of_blocks)):
    #     plt.scatter(list_of_blocks[i][0],list_of_blocks[i][1], color='green')
    #     # plt.plot([list_of_blocks[i][0], 100], [list_of_blocks[i][1], 100*asda.missiles[i]], color="yellow", linestyle="--")
    plt.show()

