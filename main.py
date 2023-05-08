from asda import Asda
from statistics import draw_distrabution, draw_scene

if __name__ == '__main__':
    asda1 = Asda(65, 100)
    asda1.place_drones(50, 120, 15, 0.8)
    asda1.place_drones(30, 130, 15, 0.8)
    asda1.place_drones(20, 105, 15, 0.8)
    result = asda1.simulate_missiles(10000)
    print(draw_distrabution(result, 50))
    draw_scene(asda1, result)
    # asda1 = Asda(65, 100, None)
    # asda1.place_drones(20, 96, 15, 0.8)
    # result = asda1.simulate_missiles(1000)
    # print(draw_distrabution(result, 1000))
    # draw_scene(asda1, result)
    # asda2 = Asda(65, 100, None)
    # asda2.place_drones(20, 95.75, 15, 0.8)
    # result = asda2.simulate_missiles(1000)
    # print(draw_distrabution(result, 1000))
    # draw_scene(asda2, result)