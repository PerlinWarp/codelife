# codelife
Alife simulations built with NumPy and Pygame. 

## Usage
```
python3 main.py
```

## Initial World (600 Lines of Code - Day 2)
#### Strongest agent - Perceptron

Each agent starts with a life of 100 frames. If agents go onto a grassy cell and eat it they get an extra 10 frames to live. Swimming in the water reduces their life by 1 frames per frame in the water. Grass grows back in a randomised way. 

After 2 days of programming, a simple program was made with a few different agents: 
* Pink - moves randomly
* White - controlled by user 
* Other - Perceptron agents with one green intensity sensing eye. 

![Perceptron agent learning](media/Perceptrons.gif)

In this gif, we see many percepron agents die but some perceptron agents finding a local minima of flying across the screen diagonally. 


## World Version 2 (1115 LOC - Day 3)
#### Strongest Agent - Reinforcement Learning 

* Added lava blocks which reduce an agent's life by 10 frames.
* Added Rock which does nothing to an agents life.
* Added a Neural Network Agent with 3 inputs (R,G,B) and 2 hidden layers which are initially random. 
* Changed the structure of the world until Perceptron agents could not learn it. 
* Added a reinforcement learning agent which uses a Look Up Table brain. 

![World 2 with Reinforcement Agents winning](https://raw.githubusercontent.com/PerlinWarp/YearOfAI/master/media/codelife_rl.gif)

### Agent Highscores (How many frames the agents lived for)
Best Random Agent Score: 50  
Best Perceptron Agent Score: 263  
Best RL_Agent Score: 670 (Input: RGB of current square)  
Best RLL_Agent Score: 2375 (RL_Agent with random choice 2% of the time)  
Best RL_Agent2 Score: 5329 (Input: RBG of current and last square colour + memory of last action)  


### TODO
Agents:
* Genetic algorithm agents
* NEAT implimentation
* Deep Reinforcement Learning Agents 
* RNN agents 
* Interactive Particle system 
* Dynamic Enviroment/grid
