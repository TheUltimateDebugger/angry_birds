class Missile:
    def __init__(self, theta, direction):
        self.theta = theta
        self.direction = direction

    def is_hitting(self, x, y):
        return self.theta * x == y and ((y > 0) == self.direction)
