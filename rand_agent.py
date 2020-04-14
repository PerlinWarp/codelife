from agent import *
import numpy as np

class Rand_agent(Agent):
    def __init__(self,x,y):
        super().__init__(x,y)
        self.type = "Random Agent"

    def live(self, grid, reward):
        # Calculate delta_x and delta_y
        delta_x = 0
        delta_y = 0
        if(random.random() < 0.01):
            delta_x = agent_size
        if(random.random() < 0.02):
            delta_x = -agent_size
        if(random.random() < 0.03):
            delta_y = agent_size
        if(random.random() < 0.04):
            delta_y = -agent_size

        super().move(delta_x,delta_y)

