from agent import *
import numpy as np

# Helper functions 
get_bin = lambda x, n: format(a, 'b').zfill(8)

def sigmoid(z):
    #Apply sigmoid activation function to scalar, vector, or matrix
    return 1/(1+np.exp(-z))

class Neural_Network():
    '''
    Code for a 2 layer neural network
    '''
    def __init__(self):        
        #Define Hyperparameters
        self.inputLayerSize = 3
        self.outputLayerSize = 2
        self.hiddenLayerSize = 3
        
        #Weights (parameters)
        self.W1 = np.random.randn(self.inputLayerSize, self.hiddenLayerSize)
        self.W2 = np.random.randn(self.hiddenLayerSize, self.outputLayerSize)
        
    def forward(self, X):
        #Propagate inputs though network
        self.z2 = np.dot(X, self.W1)
        self.a2 = self.sigmoid(self.z2)
        self.z3 = np.dot(self.a2, self.W2)
        yHat = self.sigmoid(self.z3) 
        return yHat
        
    def sigmoid(self, z):
        #Apply sigmoid activation function to scalar, vector, or matrix
        return 1/(1+np.exp(-z))


class NN_agent(Agent):
    '''
    An agent which uses a perceptron as a brain 
    Inputs are green pixel
    Ouput is x and y movements being either forward or backwards
    '''
    input_size = 1
    hidden_layer_size = 1

    def __init__(self,x,y):
        super().__init__(x,y)
        self.c = (255,random.randint(0,255),50)
        self.type = "Neural Network"
        # Make its brain
        self.brain = Neural_Network()

        self.delta_x = 0
        self.delta_y = 0

    def live(self, grid, reward):
        # Backpropagate our reward from our last action
        # max_reward = 10
        # error = max_reward - reward 
        # delta_weight_x = error * self.delta_x
        # delta_weight_y = error * self.delta_y

        # self.W_X += delta_weight_x * self.learning_rate
        # self.W_Y += delta_weight_y * self.learning_rate

        # self.delta_x = 0
        # self.delta_y = 0

        # Get our input 
        c = grid.get_cell(self.x,self.y)
        r = c.r
        g = c.g
        b = c.b

        #Get the cell infront of us
        #c = grid.get_cell(self.x,self.y)

        # Convert inputs to binary
        r = r/255
        g = g/255 # Normalise our input 
        b = b/255
        X = np.array([r, g, b])

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