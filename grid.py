import pygame
import random

import settings

w_width = settings.w_width
w_height = settings.w_height
square_size = settings.square_size
max_square_life = 100

class Square:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.life = random.random() * max_square_life

        self.r = 0
        self.g = 0
        self.b = 0

    def run(self):
        x = random.random()
        if (x < 0.4):
            self.life -= 1
        elif (x < 0.8):
            self.life += 1
        # Sanity checks
        if(self.life < 0):
            self.life = 0.0
        elif(self.life > max_square_life):
            self.life = float(max_square_life)

    def draw(self,screen):
        self.g = int( (self.life/max_square_life) * 255 )
        c = (self.r,self.g,self.b)
        pygame.draw.rect(screen, c, pygame.Rect(self.x, self.y, square_size, self.y))

class Grid:
    def __init__(self, w_width, w_height, screen):
        # Draw the grid
        cols = w_width / square_size
        rows = w_height / square_size

        self.cells = c = [[0 for i in range(rows)] for j in range(cols)]


        for i in range(0, cols):
            for j in range(0, rows):
                x = i*square_size
                y = j*square_size

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
        cell_x = x // square_size
        cell_y = y // square_size

        s = self.cells[(cell_x+1) + ((cell_y-1) * w_width)]
        print(x, s.x)
        print(y, s.y)
        return s 

    def set_cell(self,x,y,life):
        print(len(self.cells))
        x = x//10
        y = y//10

        # Convert the world position into cell position 
        print("cell_x:", x)
        print("cell_y:", y)

        s = self.cells[x-1][y-1]
        print(x, s.x)
        print(y, s.y)
        self.cells[x-1][y-1].r = 255


