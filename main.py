import constants as C
from drone import Drone
from platform import Platform
from ship import Ship
from statistics import draw_distrabution, draw_scene

if __name__ == '__main__':
    print("hello")
    drone = Drone(C.DRONE_BLOCK_PROB)
    ships = [Ship(C.R_EFFECTIVE_MISSILE, drone, C.SHIP_BLOCK_PROB, C.DRONE_SURVIVAL, C.DRONES_FOR_MISSILE) for i in range(C.NUM_OF_SHIPS)]
    platform = Platform(C.FATAL_RADIUS, C.SAFE_RADIUS, ships)
    platform.place_ship_circle(C.SHIPS_RADIUS)
    platform.simulate_missiles(100)
    draw_distrabution(platform.hits_log, 100)
    draw_scene(platform)