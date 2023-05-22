import random
import math
import time

from constants import DISTANCE_OF_DETECTION_MISSILE, MISSILE_SPEED
from drone import Drone
from enemy import Missile
from hit import Hit


class Platform:
    def __init__(self, r_100_loss, r_safe, ships=None):
        self.r_loss = r_100_loss
        self.r_safe = r_safe
        self.ships = ships
        self.missiles = []
        self.hits_log = []
        random.seed(time.time())

    def place_ship_circle(self, radius):
        theta = 2 * math.pi / len(self.ships)
        self.ships = self.ships
        for i in range(len(self.ships)):
            self.ships[i].place_ship(math.cos(theta * i) * radius, math.sin(theta * i) * radius)

    def get_crit_hit_place(self, missile):
        x1, x2 = (self.r_loss**2/(1+missile.coefficient))**0.5, -(self.r_loss**2/(1+missile.coefficient))**0.5
        if missile.is_direction_right(x1):
            return x1, x1*missile.coefficient
        else:
            return x2, x2*missile.coefficient

    def log_hit(self, missile):
        result = Hit(False, missile)
        for ship in self.ships:
            other = ship.get_hit_log(self, missile)
            if other.is_better(result):
                result = other
        if not result.is_by_drone:
            result.set_hit_point(self.get_crit_hit_place(missile))
        return result

    def generate_missile(self, num_of_missiles):
        for i in range(num_of_missiles):
            theta = random.uniform(0, 2*math.pi)
            self.missiles.append(Missile(theta))

    def calc_dist(self, coordinate):
        return math.sqrt(coordinate[0] ** 2 + coordinate[1] ** 2)

    def simulate_missiles(self, iterations):
        self.generate_missile(iterations)
        for m in self.missiles:
            self.log_hit(m)
