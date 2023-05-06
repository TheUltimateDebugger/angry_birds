import random
import math

from drone import Drone


class Asda:
    def __init__(self, r_100_loss, r_safe, drones):
        self._r_loss = r_100_loss
        self.r_safe = r_safe
        self._drones = drones

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

    @staticmethod
    def generate_missile():
        theta = random.uniform(0.0, math.pi * 2)
        m = math.tan(theta)
        return m

    def calc_dist(self, coordinate):
        return math.sqrt(coordinate[0] ** 2 + coordinate[1] ** 2)

    def simulate_missiles(self, iterations):
        sum = 0
        for i in range(iterations):
            m = self.generate_missile()
            list_of_blocks = []
            for drone in self._drones:
                if drone.missile_block_coordinate(m) != (0, 0):
                    list_of_blocks.append(drone.missile_block_coordinate(m))
            if len(list_of_blocks) > 0:
                max = self.calc_dist(list_of_blocks[0])
                for j in list_of_blocks:
                    if self.calc_dist(j) > max:
                        max = self.calc_dist(j)
                sum += self.destruction_function(max)
            else:
                sum += self.destruction_function(0)
            return 1 - sum / iterations
