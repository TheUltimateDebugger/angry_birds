import random
import math
import time

from drone import Drone


class Asda:
    def __init__(self, r_100_loss, r_safe, drones):
        self._r_loss = r_100_loss
        self.r_safe = r_safe
        self._drones = drones
        self.missiles = []
        random.seed(time.time() + random.randint(0, 100000))

    def place_drones(self, num_of_drones, distance_from_asda, drone_radius):
        theta = 2*math.pi/num_of_drones
        self._drones = []
        for i in range(num_of_drones):
            self._drones.append(Drone(math.cos(theta*i)*distance_from_asda, math.sin(theta*i)*distance_from_asda, drone_radius))


    def destruction_function(self, distance):
        if distance < self._r_loss:
            return 1
        if distance > self.r_safe:
            return 0
        return (self.r_safe-distance)/self.r_safe

    def generate_missile(self, num_of_missiles):
        for i in range(num_of_missiles):
            angle_degrees = random.uniform(0, 360)
            # Convert the angle to radians
            angle_radians = math.radians(angle_degrees)
            # theta = random.uniform(0.0, math.pi * 2)
            self.missiles.append(math.tan(angle_radians))


    def calc_dist(self, coordinate):
        return math.sqrt(coordinate[0] ** 2 + coordinate[1] ** 2)

    # def simulate_missiles_and_calculate_prob(self, iterations):
    #     sum = 0
    #     for i in range(iterations):
    #         m = self.generate_missile(iterations)
    #         list_of_blocks = []
    #         for drone in self._drones:
    #             if drone.missile_block_coordinate(m) != (0, 0):
    #                 list_of_blocks.append(drone.missile_block_coordinate(m))
    #         if len(list_of_blocks) > 0:
    #             max = self.calc_dist(list_of_blocks[0])
    #             for j in list_of_blocks:
    #                 if self.calc_dist(j) > max:
    #                     max = self.calc_dist(j)
    #             sum += self.destruction_function(max)
    #         else:
    #             sum += self.destruction_function(0)
    #         return 1 - sum / iterations

    def simulate_missiles(self, iterations):
        list_of_blocks = []
        self.generate_missile(iterations)
        for m in self.missiles:
            best = (0, 0)
            for drone in self._drones:
                if self.calc_dist(drone.missile_block_coordinate(m)) > self.calc_dist(best):
                    best = drone.missile_block_coordinate(m)
            list_of_blocks.append(best)
        return list_of_blocks


