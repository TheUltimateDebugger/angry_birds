import math

import matplotlib.pyplot as plt
from matplotlib.patches import Circle


def calc_dist(coordinate):
    return (coordinate[0] ** 2 + coordinate[1] ** 2)**0.5


def get_border(x, y, a, border):
    x1, x2 = (border ** 2 / (1 + a ** 2)) ** 0.5, -((border ** 2 / (1 + a ** 2)) ** 0.5)
    y1, y2 = x1*a, x2*a
    return (x1, y1) if (x-x1)**2+(y-y1)**2 < (x-x2)**2+(y-y2)**2 else (x2, y2)


def draw_distrabution(list_of_hits, resolution):
    distrabution = plt.figure(1)
    max_distance = 0
    for hit in list_of_hits:
        if hit.calc_dist() > max_distance:
            max_distance = hit.calc_dist()
    bucket_diff = max_distance / (resolution - 1)
    result = [0] * resolution
    losses = 0
    for hit in list_of_hits:
        if not hit.is_by_drone:
            losses += 1
        result[round(hit.calc_dist() / bucket_diff)] += 1
    x_labels = range(0, math.ceil(max_distance), math.floor(max_distance / (resolution - 1)))
    plt.xticks(range(len(x_labels)), x_labels, rotation=90)
    print("hits: " + str(losses) + " out of " + str(len(list_of_hits)))
    plt.bar(list(range(resolution)), result, align='center', alpha=0.5)
    distrabution.show()
    return result


def draw_scene(platform):
    scene = plt.figure(2)
    border = max(max((ship.x ** 2 + ship.y ** 2) ** 0.5 for ship in platform.ships), platform.r_safe) * 1.5
    for i in range(len(platform.degree_range)):
        temp = math.tan((platform.degree_range[i])) if platform.degree_range[i] <= math.pi else -math.tan((platform.degree_range[i]))
        if platform.degree_range[i] == math.pi:
            temp = -1
        if platform.degree_range[i] == 0:
            temp = 1
        b = get_border(int(temp/abs(temp)), temp, math.tan((platform.degree_range[i])), border)
        plt.plot([0, b[0]], [0, b[1]], linestyle="--", color="orange")

    platform_kill_drawing = Circle((0, 0), platform.r_loss, color='red', fill=False)
    platform_safe_drawing = Circle((0, 0), platform.r_safe, color='green', fill=False)
    # plt.margins(1, 1)
    scene.gca().add_patch(platform_kill_drawing)
    scene.gca().add_patch(platform_safe_drawing)

    for ship in platform.ships:
        ship_drawing = Circle((ship.x, ship.y), ship.radius, color='blue', fill=False)
        scene.gca().add_patch(ship_drawing)

    hits_x = []
    hits_y = []
    for hit in platform.hits_log:
        hits_x.append(hit.x)
        hits_y.append(hit.y)

    # for hit in platform.hits_log:
    #     if hit.is_by_drone:
    #         temp = get_border(hit.x, hit.y, hit.missile.coefficient, border)
    #         plt.plot([hit.x, temp[0]], [hit.y, temp[1]], color="green")

    for hit in platform.hits_log:
        if not hit.is_by_drone:
            temp = get_border(hit.x, hit.y, hit.missile.coefficient, border)
            plt.plot([hit.x, temp[0]], [hit.y, temp[1]], color="red")


    plt.scatter(hits_x, hits_y, color='green')
    # for i in range(len(list_of_blocks)):
    #     plt.scatter(list_of_blocks[i][0],list_of_blocks[i][1], color='green')
    #     # plt.plot([list_of_blocks[i][0], 100], [list_of_blocks[i][1], 100*asda.missiles[i]], color="yellow", linestyle="--")
    plt.show()
