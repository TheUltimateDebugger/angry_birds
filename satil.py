from drone import Drone


class Satil:
    def __init__(self, location, num_drones, drone_radius, prob_of_succsses) -> None:
        self.location = location
        self.num_drones = num_drones
        self.drones = []
        for i in range(num_drones):
            self.drones.append(Drone(location[0], location[1], drone_radius, prob_of_succsses))

    def get_drones(self):
        return self.drones

