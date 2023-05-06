import random
import math
class Asda:
    def __init__ (self,r_100_loss,drones):
        self._r_loss=r_100_loss
        self._drones=drones
    def destruction_function(self,x):
        if x<self
    def generate_missile(self):
        theta=random.uniform(0.0, math.pi*2)
        m=math.tan(theta)
        return m

    def calc_dist(self,coordinate):
        return math.sqrt(coordinate[0]**2+coordinate[1]**2)

    def simulate_missiles(self,iterations):
        sum=0

         for i in range (iterations):
            m=self.genarate_missile()
            list_of_blocks=[]
            for drone in self._drones:
                if drone.missile_block_coordinate()!=None:
                    list_of_blocks.append(drone.missile_block_coordinate())
            if len(list_of_blocks)>0:
                max=calc_dist(list_of_blocks[0])
                for j in list_of_blocks:
                    if calc_dist(j)>max:
                        max=calc_dist(j)
                sum+=self.destruction_function(max)
            else:
                sum+=100
            return 100-sum/iterations
                




class drone:
    def missile_block_coordinate (missile):
        pass

        

       
