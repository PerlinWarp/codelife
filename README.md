# codelife
Alife simulations built with NumPy and Pygame. 

## Usage
```
python3 main.py
```

## Initial World (600 Lines of Code)
Each agent starts with a life of 100 frames. If agents go onto a grassy cell and eat it they get an extra 10 frames to live. Swimming in the water reduces their life by 10 frames per frame in the water. Grass grows back in a randomised way. 

After 2 days of programming, a simple program was made with a few different agents: 
* Pink - moves randomly
* White - controlled by user 
* Other - Perceptron agents with one green intensity sensing eye. 

![Perceptron agent learning](media/Perceptrons.gif)

In this gif, we see many percepron agents die but some perceptron agents finding a local minima of flying across the screen diagonally. 

### TODO
Agents:
* Multi Layer Neural Network agents with Backprop 
* Genetic algorithm agents
* NEAT implimentation
* Reinforcement Learning Agents 
* RNN agents 