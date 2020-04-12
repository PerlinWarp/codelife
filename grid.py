import pygame
import random

from materials import *
import settings

w_width = settings.w_width
w_height = settings.w_height
square_size = settings.square_size


class Grid:
    def __init__(self, w_width, w_height, screen):
        # Draw the grid
        cols = w_width // square_size
        rows = w_height // square_size

        self.cells = [[0 for i in range(rows)] for j in range(cols)]


        for i in range(0, cols):
            for j in range(0, rows):
                x = i*square_size
                y = j*square_size

                if (random.random() * x < 0.8 * y):
                    self.cells[i][j] = (Water(x,y))
                else:
                    self.cells[i][j] = (Square(x,y))
    
    def run(self):
        for i in self.cells:
            for c in i:
                c.run()
    
    def draw(self,screen):
        for i in self.cells:
            for c in i:
                c.draw(screen)

    def get_cell(self,x,y):
        # Convert the world position into cell position 
        x = x//square_size
        y = y//square_size

        s = self.cells[x][y]
        return s 

    def set_cell(self,x,y,life):
        x = x//square_size
        y = y//square_size

        # Convert the world position into cell position 
        print("cell_x:", x, "/",len(self.cells[0]))
        print("cell_y:", y, "/", len(self.cells))

        s = self.cells[x][y]
        s.life -= life;
        self.cells[x][y].r = 255


