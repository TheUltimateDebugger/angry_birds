from asda import Asda
from statistics import draw_distrabution, draw_scene

if __name__ == '__main__':
    asda = Asda(65, 67, None)
    asda.place_drones(12, 100, 100)
    print(asda.simulate_missiles(500))
    result = asda.simulate_missiles(500)
    print(draw_distrabution(result, 1000))
    draw_scene(asda, result)