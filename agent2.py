from agent import *
import numpy as np

get_bin = lambda x, n: format(a, 'b').zfill(8)



class Agent2(Agent):
    def __init__(self,x,y):
        super().__init__(x,y)
        self.type = "Agent2"

    def live(self, grid, reward):
        c = grid.get_cell(self.x,self.y)
        r = c.r
        g = c.g
        b = c.b

        #Get the cell infront of us
        #c = grid.get_cell(self.x,self.y)

        # Convert to binary
        a = np.array([g], dtype=np.uint8)
        a = np.unpackbits(a)



        # Calculate delta_x and delta_y
        delta_x = 0
        delta_y = 0
        if(random.random() < 0.01):
            delta_x = agent_size
        if(random.random() < 0.09):
            delta_x = -agent_size
        if(random.random() < 0.03):
            delta_y = agent_size
        if(random.random() < 0.04):
            delta_y = -agent_size

        super().move(delta_x,delta_y)

