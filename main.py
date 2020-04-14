import pygame
import numpy as np
import random

import settings
from grid import Grid
from agent import Agent
from agent2 import Agent2
from player_agent import Player
from gen_agent import Gen_agent
from p_agent import P_agent
from rl_agent import RL_agent, RL_agent2, RRL_agent

pygame.init()
w_width = settings.w_width
w_height = settings.w_height
screen = pygame.display.set_mode((w_width, w_height))
done = False

# Making our world
grid = Grid(w_width, w_height, screen)
grid.draw(screen)

# Making an agent
agent = Agent2(0, w_height//2)
player = Player(w_width//2, w_height//2)
agents = [agent, player]

# Make the genetic agents
for i in range(0,10):
    agents.append(P_agent(random.randint(0,w_width), random.randint(0,w_height)))

for i in range(0,10):
    agents.append(RL_agent(random.randint(0,w_width), random.randint(0,w_height),grid))

for i in range(0,10):
    agents.append(RL_agent2(random.randint(0,w_width), random.randint(0,w_height),grid))

for i in range(0,10):
    agents.append(RRL_agent(random.randint(0,w_width), random.randint(0,w_height),grid))

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

        pygame.display.flip()