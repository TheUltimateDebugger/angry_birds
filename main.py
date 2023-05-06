from asda import Asda

if __name__ == '__main__':
    asda = Asda(65, 66, None)
    asda.place_drones(10, 66, 10)
    print(asda.simulate_missiles(1000))