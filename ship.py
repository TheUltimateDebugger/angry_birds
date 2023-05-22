from drone import Drone


class Ship:
    def __init__(self, x, y, num_of_drones, drone_speed, color="blue") -> None:
        self.x = x
        self.y = y
        self.drones = []
        self.color = color
        self.num_of_drones = num_of_drones