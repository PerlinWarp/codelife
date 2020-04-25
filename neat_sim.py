import pygame
import numpy as np
import random
import neat
import os

import settings
from grid import Grid
from agent import Agent
from rand_agent import Rand_agent
from player_agent import Player, Player2
from gen_agent import Gen_agent, Population
from p_agent import P_agent
from rl_agent import RL_agent, RL_agent2, RRL_agent
import neat_agent

# Get the NEAT config file
local_dir = os.path.dirname(__file__)
config_path = os.path.join(local_dir, "config-feedforward.txt")
config = neat.config.Config(neat.DefaultGenome, neat.DefaultReproduction,
                    neat.DefaultSpeciesSet, neat.DefaultStagnation,
                    config_path)

def main(genomes, config):
    pygame.init()
    w_width = settings.w_width
    w_height = settings.w_height
    screen = pygame.display.set_mode((w_width, w_height))
    done = False

    # Making our world
    grid = Grid(w_width, w_height, screen)
    grid.draw(screen)


    # # Making an agent
    # agent =  Rand_agent(w_width//2, w_height//2)
    # player = Player2(w_width//2, w_height//2)
    # agents = [agent, player]


    # # Make a population of genetic agents
    genetic_agents = neat_agent.Population(grid, screen, genomes, config)

    while not done:
            for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                            quit()

            # Run the world
            grid.run()
            grid.draw(screen)

            # Run the genetic agents
            done = genetic_agents.run()

            pygame.display.flip()

# Create a population
p = neat.Population(config)

# Stats reporter
p.add_reporter(neat.StdOutReporter(True))
stats = neat.StatisticsReporter()
p.add_reporter(stats)

winner = p.run(main,500)
# Display the winning genome.
print('\nBest genome:\n{!s}'.format(winner))