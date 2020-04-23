import pygame
import numpy as np
import random

import settings
from grid import Grid
from agent import Agent
from rand_agent import Rand_agent
from player_agent import Player, Player2
from gen_agent import Gen_agent, Population
from p_agent import P_agent
from rl_agent import RL_agent, RL_agent2, RRL_agent
import q_agent

pygame.init()
w_width = settings.w_width
w_height = settings.w_height
screen = pygame.display.set_mode((w_width, w_height))
done = False

# Making our world
grid = Grid(w_width, w_height, screen)
grid.draw(screen)

# Making an agent
agent =  Rand_agent(0, w_height//2)
player = Player2(w_width//2, w_height//2)
agents = [agent, player]


# # Make a population of genetic agents
genetic_agents = q_agent.Population(10, grid, screen)

while not done:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        done = True

        # Run the world
        grid.run()
        grid.draw(screen)

        # Run the agents
        for agent in agents:
            if (agent):
                if (agent.life < 1):
                        print("Agent:", agent.type, "died after: ", agent.alive_time)
                        print(len(agents)-1,"still alive")
                        agents.remove(agent)
                        del agent
                else:
                    agent.run(grid)
                    agent.draw(screen)

        # Run the genetic agents
        genetic_agents.run()

        pygame.display.flip()

genetic_agents.stats()