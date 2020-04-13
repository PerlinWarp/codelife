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
        # Define Hyperparameters
        self.inputLayerSize = 3
        self.outputLayerSize = 2
        self.hiddenLayerSize = 3
        
        # Weights (parameters)
        self.W1 = np.random.randn(self.inputLayerSize, self.hiddenLayerSize)
        self.W2 = np.random.randn(self.hiddenLayerSize, self.outputLayerSize)
        
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

    def sigmoid_prime(self, z):
        # Derivative of our sigmoid function
        retrurn np.exp(-z)/(1+np.exp(-z)**2)

    def cost_func_prime(self, X, y):
        '''
        We assume the error function here is max reward - reward 
        Compute derivative with respect to W and W2 for a given X and y:
        '''
        self.yHat = self.forward(X)
        
        delta3 = np.multiply(-(y-self.yHat), self.sigmoidPrime(self.z3))
        dJdW2 = np.dot(self.a2.T, delta3)
        
        delta2 = np.dot(delta3, self.W2.T)*self.sigmoidPrime(self.z2)
        dJdW1 = np.dot(X.T, delta2)  
        
        return dJdW1, dJdW2

    def compute_gradients(self, X, y):
        dJdW1, dJdW2 = self.cost_func_prime(X, y)
        return np.concatenate((dJdW1.ravel(), dJdW2.ravel()))


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
        max_reward = 10
        '''
        We do not just want to predict 10 all the time. 
        '''
        dJdW1, dJdW2 = self.brain.cost_func_prime(X, max_reward)

        # Update our weights
        scalar = 3
        NN.W1 = NN.W1 + scalar*dJdW1
        NN.W2 = NN.W2 + scalar*dJdW2


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