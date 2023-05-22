import random

from drone import Drone
from hit import Hit


class Ship:
    def __init__(self, x, y, effective_radius, drone, prob_of_working, prob_of_surviving, drones_for_missile,
                 color="blue") -> None:
        self.x = x
        self.y = y
        self.color = color
        self.drones_used = 0
        self.drone = drone
        self.prob_of_surviving = prob_of_surviving
        self.radius = effective_radius
        self.prob_of_working = prob_of_working
        self.drones_for_missile = drones_for_missile

    def __init__(self, effective_radius, drone, prob_of_working, prob_of_surviving, drones_for_missile,
                 color="blue") -> None:
        self.color = color
        self.drones_used = 0
        self.drone = drone
        self.prob_of_surviving = prob_of_surviving
        self.radius = effective_radius
        self.prob_of_working = prob_of_working
        self.drones_for_missile = drones_for_missile

    def place_ship(self, x, y):
        self.x = x
        self.y = y

    def did_ship_work(self):
        return random.uniform(0, 1) <= self.prob_of_working

    def update_num_of_drones(self):
        self.drones_used += self.drones_for_missile * self.drones_for_missile

    def get_hit_log(self, platform, missile):
        a = missile.coefficient ** 2 + 1
        b = -2 * self.x - 2 * self.y * missile.coefficient
        c = self.x ** 2 + self.y ** 2 - self.radius ** 2
        if b ** 2 < 4 * a * c:
            return Hit(0, 0, False, missile)
        if not self.did_ship_work():
            return Hit(0, 0, False, missile)
        if random.uniform(0, 1) > (1 - self.drone.prob_of_successes ** self.drones_for_missile):
            return Hit(0, 0, False, missile)

        self.update_num_of_drones()

        x1 = (-b + (b ** 2 - 4 * a * c) ** 0.5) / (2 * a)
        x2 = (-b - (b ** 2 - 4 * a * c) ** 0.5) / (2 * a)

        if not missile.is_direction_right(x1):
            return Hit(x2, missile.coefficient * x2, True, missile)

        if not missile.is_direction_right(x2):
            return Hit(x1, missile.coefficient * x1, True, missile)

        if x1 ** 2 + (x1 * missile.coefficient) ** 2 > x2 ** 2 + (x2 * missile.coefficient) ** 2:
            return Hit(x1, missile.coefficient * x1, True, missile)
        else:
            return Hit(x2, missile.coefficient * x2, True, missile)
