from agent import *
import numpy as np

get_bin = lambda x, n: format(a, 'b').zfill(8)



class Player(Agent):
    def __init__(self,x,y):
        super().__init__(x,y)
        self.c = (255,255,255)

    def live(self, grid):
        # Calculate delta_x and delta_y
        delta_x = 0
        delta_y = 0

        # Infinite life
        self.life += 10
        
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_UP]: delta_y -= 3
        if pressed[pygame.K_DOWN]: delta_y += 3
        if pressed[pygame.K_LEFT]: delta_x -= 3
        if pressed[pygame.K_RIGHT]: delta_x += 3

        super().move(delta_x,delta_y)

