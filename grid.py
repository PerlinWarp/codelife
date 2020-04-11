import pygame
import random

square_size = 10
max_square_life = 100

class Square:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.life = random.random() * max_square_life

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
        g = int( (self.life/max_square_life) * 255 )
        c = (0,g,0)
        pygame.draw.rect(screen, c, pygame.Rect(self.x, self.y, self.x+square_size, self.y+square_size))



class Grid:
    def __init__(self, w_width, w_height, screen):
        self.cells = []
        # Draw the grid
        cols = w_width / square_size
        rows = w_height / square_size

        for i in range(0, cols):
            for j in range(0, rows):
                x = i*square_size
                y = j*square_size

                self.cells.append(Square(x,y))
    
    def run(self):
        for i in self.cells:
            i.run()
    
    def draw(self,screen):
        for i in self.cells:
            i.draw(screen)

