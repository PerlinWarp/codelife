import pygame
import numpy as np

import settings
from grid import Grid
from agent import Agent

pygame.init()
w_width = settings.w_width
w_height = settings.w_height
screen = pygame.display.set_mode((w_width, w_height))
done = False

# Making our world
grid = Grid(w_width, w_height, screen)
grid.draw(screen)

# Making an agent
agent = Agent(w_width-11, w_height-11)

while not done:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        done = True

        # Run the world
        grid.run()
        grid.draw(screen)

        # Run the agent
        agent.run(grid)
        agent.draw(screen)

        pygame.display.flip()