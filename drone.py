import random


class Drone:
    def __init__(self, prob_of_successes):
        self.prob_of_successes = prob_of_successes

    def is_blocking(self):
        return random.uniform(0, 1) <= self.prob_of_successes


    # def missile_block_coordinate(self, missile):
    #     a = missile.theata**2+1
    #     b = -2*self.x-2*self.y*missile.theata
    #     c = self.x**2 + self.y**2 - self.radius**2
    #     if b**2 < 4*a*c or self.y * missile.direction < 0 or random.uniform(0, 1) > self.prob_of_successes:
    #         return 0, 0
    #     x1 = (-b+(b**2-4*a*c)**0.5)/(2*a)
    #     x2 = (-b-(b**2-4*a*c)**0.5)/(2*a)
    #     if x1 ** 2 + (x1 * missile.theata) ** 2 > x2 ** 2 + (x2 * missile.theata) ** 2:
    #         return x1, x1 * missile.theata
    #     return x2, x2 * missile.theata
