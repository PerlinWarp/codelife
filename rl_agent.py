from agent import *
import numpy as np

# Helper functions 
get_bin = lambda x, n: format(a, 'b').zfill(8)

def sigmoid(z):
    #Apply sigmoid activation function to scalar, vector, or matrix
    return 1/(1+np.exp(-z))


class RL_agent(Agent):
    '''
    An agent which uses a perceptron as a brain 
    Inputs are green pixel
    Ouput is x and y movements being either forward or backwards
    '''
    input_size = 1
    hidden_layer_size = 1

    def __init__(self,x,y):
        super().__init__(x,y)
        self.type = "RL"
        self.c = (random.randint(0,255),random.randint(0,255),255)

        # Weights of the neural network
        self.W_X = random.random()
        self.W_Y = random.random()
        self.learning_rate = 0.01

        self.delta_x = 0
        self.delta_y = 0

    def live(self, grid, reward):
        # Backpropagate our reward from our last action
        max_reward = 10
        error = max_reward - reward 
        delta_weight_x = error * self.delta_x
        delta_weight_y = error * self.delta_y

        self.W_X += delta_weight_x * self.learning_rate
        self.W_Y += delta_weight_y * self.learning_rate

        self.delta_x = 0
        self.delta_y = 0

        # Get our input 
        c = grid.get_cell(self.x,self.y)
        r = c.r
        g = c.g
        b = c.b

        #Get the cell infront of us
        #c = grid.get_cell(self.x,self.y)

        # Convert inputs to binary
        a = g/255 # Normalise our input 
        print("a: ", a)

        # Propagate through the net 
        x_out = a * self.W_X
        y_out = a * self.W_Y

        #x_out = sigmoid(x_out)
        #y_out = sigmoid(y_out)

        print(x_out, y_out)

        # Prediction
        if(x_out > 0):
            self.delta_x = agent_size
        else:
            self.delta_x = -agent_size

        if (y_out > 0):
            self.delta_y = agent_size
        else:
            self.delta_y = -agent_size

        super().move(self.delta_x,self.delta_y)

class P_agent2(Agent):
    '''
    An agent which uses a perceptron as a brain 
    Inputs are green pixel
    Ouput is x and y movements being either forward or backwards
    '''
    input_size = 1
    hidden_layer_size = 1

    def __init__(self,x,y):
        super().__init__(x,y)
        self.c = (random.randint(0,255),random.randint(0,255),255)

        # Weights of the neural network
        self.W_X = random.random()
        self.W_Y = random.random()
        self.learning_rate = 0.01

        self.delta_x = 0
        self.delta_y = 0

    def live(self, grid, reward):
        # Backpropagate our reward from our last action
        max_reward = 10
        error = max_reward - reward 
        delta_weight_x = error * self.delta_x
        delta_weight_y = error * self.delta_y

        self.W_X += delta_weight_x * self.learning_rate
        self.W_Y += delta_weight_y * self.learning_rate

        self.delta_x = 0
        self.delta_y = 0

        # Get our input 
        c = grid.get_cell(self.x,self.y)
        r = c.r
        g = c.g
        b = c.b

        #Get the cell infront of us
        #c = grid.get_cell(self.x,self.y)

        # Convert inputs to binary
        print("C:", c)
        a = g/255 # Normalise our input 
        print("a: ", a)

        # Propagate through the net 
        x_out = a * self.W_X
        y_out = a * self.W_Y

        #x_out = sigmoid(x_out)
        #y_out = sigmoid(y_out)

        print(x_out, y_out)

        # Prediction
        if(x_out > 0):
            self.delta_x = agent_size
        else:
            self.delta_x = -agent_size

        if (y_out > 0):
            self.delta_y = agent_size
        else:
            self.delta_y = -agent_size

        super().move(self.delta_x,self.delta_y)