import math


class Missile:
    def __init__(self, theta):
        if theta >= math.pi:
            self.direction = False
        else:
            self.direction = True
        self.coefficient = math.tan(theta)

    def is_hitting(self, x, y):
        return self.coefficient * x == y and ((y > 0) == self.direction)

    def is_direction_right(self, x):
        return (x * self.coefficient > 0) == self.direction
