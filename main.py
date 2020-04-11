import pygame
import numpy as np
from grid import Grid

pygame.init()
w_width = 800
w_height = 600
screen = pygame.display.set_mode((w_width, w_height))
done = False

grid = Grid(w_width, w_height, screen)
grid.draw(screen)

while not done:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        done = True

        # Run the world
        grid.run()
        grid.draw(screen)

        pygame.display.flip()