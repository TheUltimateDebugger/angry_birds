import math

import numpy as np


class Drone:
    def __init__(self, x, y, radius):
        self.x = x
        self.y = y
        self.radius = radius

    def missile_block_coordinate(self, missile):
        a = missile**2+1
        b = -2*self.x-2*self.y*missile
        c = self.x**2 + self.y**2 - self.radius**2
        if b**2 < 4*a*c:
            return 0, 0
        x1 = (-b+(b**2-4*a*c)**0.5)/(2*a)
        x2 = (-b-(b**2-4*a*c)**0.5)/(2*a)
        if x1 ** 2 + (x1 * missile) ** 2 > x2 ** 2 + (x2 * missile) ** 2:
            return x1, x1 * missile
        return x2, x2 * missile
