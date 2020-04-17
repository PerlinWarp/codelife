from agent import *
from agent2 import Agent2
import numpy as np

get_bin = lambda x, n: format(a, 'b').zfill(8)


class Player(Agent):
    def __init__(self,x,y):
        super().__init__(x,y)
        self.type = "Player"
        self.c = (255,255,255)

    def live(self, grid, reward):
        # Calculate delta_x and delta_y
        delta_x = 0
        delta_y = 0

        # DEBUG: Infinite life
        ##self.life += 10
        
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_UP]: delta_y -= 3
        if pressed[pygame.K_DOWN]: delta_y += 3
        if pressed[pygame.K_LEFT]: delta_x -= 3
        if pressed[pygame.K_RIGHT]: delta_x += 3

        super().move(delta_x,delta_y)

class Player2(Agent2):
    def __init__(self,x,y):
        super().__init__(x,y)
        self.type = "Player2"
        self.c = (255,255,255)

    def live(self, grid, reward):
        # Calculate delta_x and delta_y
        delta_x = 0
        delta_y = 0

        # DEBUG: Infinite life
        self.life += 10
        
        pressed = pygame.key.get_pressed()
        action = None
        if pressed[pygame.K_UP]: action = "forward"
        if pressed[pygame.K_LEFT]: action = "left"
        if pressed[pygame.K_RIGHT]: action = "right"

        super().move(action)
