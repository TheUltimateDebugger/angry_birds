import math


class Missile:
    def __init__(self, theta):
        self.direction = False
        if theta%(2*math.pi) >= math.pi:
            self.direction = False
        else:
            self.direction = True
        self.coefficient = math.tan(theta)

    def is_hitting(self, x, y):
        return self.coefficient * x == y and self.is_direction_right(x)

    def is_direction_right(self, x):
        return (x * self.coefficient > 0) == self.direction

    def __str__(self):
        return str(self.coefficient) + " " + ("+" if self.direction else "-")