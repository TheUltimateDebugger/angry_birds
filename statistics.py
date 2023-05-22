import math

import matplotlib.pyplot as plt
from matplotlib.patches import Circle


def calc_dist(coordinate):
    return math.sqrt(coordinate[0] ** 2 + coordinate[1] ** 2)

def draw_distrabution(list_of_hits, resolution):
    max_distance = 0
    for block in list_of_hits:
        if calc_dist(block) > max_distance:
            max_distance = calc_dist(block)
    bucket_diff = max_distance / (resolution - 1)
    result = [0] * resolution
    for hit in list_of_hits:
        result[round(calc_dist(hit.calc_dist) / bucket_diff)] += 1
    print(result[0])
    print(result[0]/10000)
    plt.bar(list(range(resolution)), result, align='center', alpha=0.5)
    plt.show()
    return result

def draw_scene(platform):
    platform_kill_drawing = Circle((0, 0), platform._r_loss, color='red', fill=True)
    platform_safe_drawing = Circle((0, 0), platform.r_safe, color='green', fill=False)
    # plt.margins(1, 1)
    plt.gca().add_patch(platform_kill_drawing)
    plt.gca().add_patch(platform_safe_drawing)

    for ship in platform.ships:
        ship_drawing = Circle((ship.x, ship.y), ship.radius, color='blue', fill=False)
        plt.gca().add_patch(ship_drawing)

    hits_x = []
    hits_y = []
    for hit in platform.hits_log:
        hits_x.append(hit.x)
        hits_y.append(hit.y)

    drone_drawing = Circle((platform.satil.location[0], platform.satil.location[1]), 10, color='blue', fill=True)
    plt.gca().add_patch(drone_drawing)
    plt.scatter(hits_x, hits_y, color='green')
    # for i in range(len(list_of_blocks)):
    #     plt.scatter(list_of_blocks[i][0],list_of_blocks[i][1], color='green')
    #     # plt.plot([list_of_blocks[i][0], 100], [list_of_blocks[i][1], 100*asda.missiles[i]], color="yellow", linestyle="--")
    plt.show()

