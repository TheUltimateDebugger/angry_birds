import random
import math
import time

from constants import DISTANCE_OF_DETECTION_MISSILE, MISSILE_SPEED
from drone import Drone
from hit import Hit
from missile import Missile


class Platform:
    def __init__(self, r_100_loss, r_safe, degree_range, ships=None):
        self.r_loss = r_100_loss
        self.r_safe = r_safe
        self.degree_range = degree_range
        self.ships = ships
        self.missiles = []
        self.hits_log = []
        random.seed(time.time())

    def place_ship_circle(self, radius):
        theta = (self.degree_range[1] - self.degree_range[0]) / (len(self.ships))
        for i in range(len(self.ships)):
            dx = 1 if (theta * i + self.degree_range[0] + 0.5*theta) % (2*math.pi) < 0.5 * math.pi else -1
            dy = 1 if (theta * i + self.degree_range[0] + 0.5*theta) % (2*math.pi) < math.pi else -1
            self.ships[i].place_ship(math.cos(theta * i + self.degree_range[0] + 0.5*theta) * radius * dx,
                                     math.sin(theta * i + self.degree_range[0] + 0.5*theta) * dy * radius)

    def place_ship_circle_smart(self):
        self.place_ship_circle((self.r_safe**2-self.ships[0].radius**2)**0.5)

    def get_crit_hit_place(self, missile):
        x1, x2 = (self.r_loss ** 2 / (1 + missile.coefficient ** 2)) ** 0.5, -(
                    (self.r_loss ** 2 / (1 + missile.coefficient ** 2)) ** 0.5)
        if missile.is_direction_right(x1):
            return x1 * missile.coefficient, x1
        else:
            return x2 * missile.coefficient, x2

    def log_hit(self, missile):
        result = Hit(0, 0, False, missile)
        for ship in self.ships:
            other = ship.get_hit_log(self, missile)
            if other.is_better(result):
                result = other
        if not result.is_by_drone:
            result.set_hit_point(self.get_crit_hit_place(missile))
        self.hits_log.append(result)
        return result

    def generate_missile(self, num_of_missiles):
        for i in range(num_of_missiles):
            theta = random.uniform(self.degree_range[0], self.degree_range[1])
            self.missiles.append(Missile(theta))

    def calc_dist(self, coordinate):
        return math.sqrt(coordinate[0] ** 2 + coordinate[1] ** 2)

    def get_drone_used(self):
        sum = 0
        for ship in self.ships:
            sum += ship.drones_used
        return sum

    def simulate_missiles(self, iterations):
        self.generate_missile(iterations)
        for m in self.missiles:
            self.log_hit(m)
