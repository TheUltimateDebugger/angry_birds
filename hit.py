class Hit:
    def __init__(self, y, x, is_by_drone, missile):
        self.x = x
        self.y = y
        self.is_by_drone = is_by_drone
        self.missile = missile

    def set_hit_point(self, coord):
        self.x = coord[0]
        self.y = coord[1]
    def is_better(self, other):
        return self.x ** 2 + self.y ** 2 > other.x ** 2 + other.y ** 2

    def calc_dist(self):
        return (self.x ** 2 + self.y ** 2)**0.5

    def __str__(self):
        return "(" + str(self.x) + ", " + str(self.y) + ") " + ("V" if self.is_by_drone else "X") + " " + str(self.missile)