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

### New Agent (1650 LOC)
An Agent should be able to see more than just the cell it is on to make a proper decision about where to go.
This caused me to make a new agent, which can sense the colour of the block it is standing on but also has an antenna which allows it to sense the block infront. It can then move either forwards or turn either left or right. 

I expected this to give a much greater performance as an agent would be able to look at all the blocks surrounding it and always pick the best option. 

#### A problem emerges. 
To test out the new agent, I tried it with my best performing agent's brain, RL2, but this newly formed agent often comes into a problem where it just spins around repeating a sequence of actions.

![Pink RL Agent stuck spinning in a circle](https://raw.githubusercontent.com/PerlinWarp/YearOfAI/master/media/Spinning.gif) 

Above we see the pink agent is stuck in this spinning loop. 

The reason this was happening:  
When the RL agent looks up what to do given its sensory input in its memory, it gets the expected rewards for each action it could take, then takes the action which would give it the highest reward.   

The problem is, all these values were the same, due to me initialising expected rewards to 0. So when the sensory input for neighbouring squares was the same, since the rewards were the same, it would pick the left, get a negative reward, pick forward, get a negative reward, pick left, get a negative reward, pick right...  Initialising the values randomly, fixed this problem. 

## Q Learning
My best performing RL agents before this point, only cared about immediate reward. Given that an agent could:
* see a half dead grass patch and move onto it immeditely
* see a half dead grass patch, rotate left and right, see a fully live grass patch and move onto it. 

I thought that being able make decisions based on long term reward would help a new type of agent beat the 5329 frame high score. Excited at this prospect, I decided to code a new agent which uses a Q Table to make decisions. 

![Q Learning Equation](https://wikimedia.org/api/rest_v1/media/math/render/svg/678cb558a9d59c33ef4810c9618baf34a9577686)

This new type of agent now has some parameters, which I decided to optimise using a genetic algorithm. I track the max, min and average scores of each generation and plot them when I exit the simulation, however the results were not what I was looking for:  

![My genetic algorithm failing to optimise parameters](https://raw.githubusercontent.com/PerlinWarp/YearOfAI/master/media/QTableGA.png)


### TODO
Agents:
* NEAT implimentation
* Deep Reinforcement Learning Agents 
* RNN agents 
* Interactive Particle system 
* Dynamic Enviroment/grid

