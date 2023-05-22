class Hit:
    def __init__(self, y, x, is_by_drone, missile):
        self.x = x
        self.y = y
        self.is_by_drone = is_by_drone
        self.missile = missile
    def __init__(self, is_by_drone, missile):
        self.is_by_drone = is_by_drone
        self.missile = missile

    def is_better(self, other):
        return self.x**2 + self.y**2 > other.x**2 + other.y**2