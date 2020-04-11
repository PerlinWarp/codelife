import pygame
import random

import settings

w_width = settings.w_width
w_height = settings.w_height
square_size = settings.square_size
agent_size = square_size

class Agent:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.life = 100

    def eat(self, grid):
        grid.set_cell(self.x,self.y,0) 

    def move(self):
        if(random.random() < 0.2):
            self.x += agent_size
        if(random.random() < 0.2):
            self.x -= agent_size
        if(random.random() < 0.2):
            self.y += agent_size
        if(random.random() < 0.2):
            self.y -= agent_size

        # Sanity checks
        if(self.x < 0):
            self.x = 0
        if(self.y < 0):
            self.y = 0
        if (self.x + agent_size > w_width):
            self.x = w_width 
        if (self.y + agent_size> w_height):
            self.y = w_height

    def run(self, grid):
        self.current_cell_x = self.x // square_size
        self.current_cell_y = self.y //square_size
        self.move()
        self.eat(grid)

    def draw(self,screen):
        pygame.draw.rect(screen, (0,0,255), pygame.Rect(self.x, self.y, square_size, square_size))