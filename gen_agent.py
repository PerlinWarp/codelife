from agent import *
from settings import w_height
import numpy as np
import copy

# Helper functions 
get_bin = lambda x, n: format(a, 'b').zfill(8)

def sigmoid(z):
    #Apply sigmoid activation function to scalar, vector, or matrix
    return 1/(1+np.exp(-z))

class Neural_Network():
    '''
    Code for a 2 layer neural network
    '''
    def __init__(self, W1=None, W2=None):        
        # Define Hyperparameters
        self.inputLayerSize = 6
        self.outputLayerSize = 2
        self.hiddenLayerSize = 8
        
        # Weights (parameters)
        if (W1 is None):
            self.W1 = np.random.randn(self.inputLayerSize, self.hiddenLayerSize)
            self.W2 = np.random.randn(self.hiddenLayerSize, self.outputLayerSize)
        else:
            self.W1 = W1
            self.W2 = W2
        
    def forward(self, X):
        # Propagate inputs though network
        self.z2 = np.dot(X, self.W1)
        self.a2 = self.sigmoid(self.z2)
        self.z3 = np.dot(self.a2, self.W2)
        yHat = self.sigmoid(self.z3) 
        return yHat
        
    def sigmoid(self, z):
        # Apply sigmoid activation function to scalar, vector, or matrix
        return 1/(1+np.exp(-z))


class Gen_agent(Agent):
    '''
    An agent which uses a perceptron as a brain 
    Inputs are green pixel
    Ouput is x and y movements being either forward or backwards
    '''
    input_size = 1
    hidden_layer_size = 1

    def __init__(self,x,y, brain=None):
        super().__init__(x,y)
        self.c = (255,random.randint(0,255),50)
        self.type = "Genetic Network"
        # Make its brain
        if (brain):
            self.brain = brain
        else:
            # Make a new brain
            self.brain = Neural_Network()

        self.delta_x = 0
        self.delta_y = 0

    def live(self, grid, reward):
        # Get our input 
        c = grid.get_cell(self.x,self.y)
        c_up = grid.get_cell(self.x, (self.y+10)%w_height)
        X = np.array([c.r,c.g,c.b,c_up.r, c_up.g, c_up.b]) / 255

        # Propagate through the net 
        out = self.brain.forward(X)
        x_out = out[0]
        y_out = out[1]
        #print(x_out, y_out)

        # Prediction
        if(x_out > 0.5):
            self.delta_x = agent_size
        else:
            self.delta_x = -agent_size

        if (y_out > 0.5):
            self.delta_y = agent_size
        else:
            self.delta_y = -agent_size

        super().move(self.delta_x,self.delta_y)

class Population():
    def __init__(self, size, grid, screen):
        self.size = size
        self.grid = grid
        self.screen = screen
        self.agents = []
        for s in range(size):
            x = random.randint(0,w_width-10)
            y = random.randint(0,w_height-10)
            self.agents.append(Gen_agent(x,y))

    def cross_over(self,a,b):
        #https://stackoverflow.com/questions/53398027/multipoint-crossover-using-numpy
        sieve = np.random.randint(2, size=a.shape)
        not_sieve=sieve^1 
        co = a*sieve + b*not_sieve
        return co

    def breed(self):
        # Returns a new population
        babies = []
        dad = self.agents[0]
        mum = self.agents[1]

        # W1 = (dad.brain.W1 + mum.brain.W1)/2
        # W2 = (dad.brain.W2 + mum.brain.W2)/2
        W1 = self.cross_over(dad.brain.W1, mum.brain.W1)
        W2 = self.cross_over(dad.brain.W2, mum.brain.W2)

        newborn_brain = Neural_Network(W1, W2)
        for i in range(5):
            x = random.randint(0,w_width-10)
            y = random.randint(0,w_height-10)
            baby = Gen_agent(x,y,newborn_brain)
            babies.append(baby)


        for s in range(5):
            x = random.randint(0,w_width-10)
            y = random.randint(0,w_height-10)
            babies.append(Gen_agent(x,y))
        return babies

    def run(self):
        if not(len(self.agents) < 3):
            for agent in self.agents:
                if (agent.life < 1):
                        print("Agent:", agent.type, "died after: ", agent.alive_time)
                        print(len(self.agents)-1,"still alive")
                        self.agents.remove(agent)
                        del agent
                else:
                    agent.run(self.grid)
                    agent.draw(self.screen)
        else:
            # Breed em
            print("New Population")
            babies = self.breed()
            print(babies)
            self.agents = babies


