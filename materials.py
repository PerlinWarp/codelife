import pygame
import random

import settings

class Square:
    size = settings.square_size
    max_life = 100

    def __init__(self,x,y):
        self.type = "Square"
        self.x = x
        self.y = y

        self.life = random.random() * Square.max_life

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
        elif(self.life > Square.max_life):
            self.life = float(Square.max_life)

    def draw(self,screen):
        self.g = int( (self.life/Square.max_life) * 255 )
        c = (self.r,self.g,self.b)
        pygame.draw.rect(screen, c, pygame.Rect(self.x, self.y, Square.size, Square.size))
        self.r = 0

class Water(Square):
    def __init__(self,x,y):
        super().__init__(x,y)
        self.type = "Water"
        self.life = 0
        self.r = 0
        self.g = 0
        self.b = 120

    def run(self):
        return

    def draw(self,screen):
        c = (self.r,self.g,self.b)
        pygame.draw.rect(screen, c, pygame.Rect(self.x, self.y, Square.size, Square.size))
