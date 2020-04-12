from agent import *
import numpy as np

# Helper functions 
get_bin = lambda x, n: format(a, 'b').zfill(8)

def sigmoid(z):
    #Apply sigmoid activation function to scalar, vector, or matrix
    return 1/(1+np.exp(-z))


class Gen_agent(Agent):
    def __init__(self,x,y):
        super().__init__(x,y)
        self.c = (random.randint(0,255),random.randint(0,255),255)
        self.reward = 0

    def live(self, grid, reward):
        c = grid.get_cell(self.x,self.y)
        r = c.r
        g = c.g
        b = c.b

        #Get the cell infront of us
        #c = grid.get_cell(self.x,self.y)

        # Convert to binary
        a = np.array([g], dtype=np.uint8)
        A = np.unpackbits(a)

        # Weights of the neural network
        input_size = len(A)
        hidden_layer_size = 1
        W_X = np.random.randn(input_size, hidden_layer_size)
        W_Y = np.random.randn(input_size, hidden_layer_size)


        # Propagate through the net 
        x1 = np.dot(A, W_X)
        y1 = np.dot(A, W_Y)

        x_out = sigmoid(x1)
        y_out = sigmoid(y1)

        # Prediction
        delta_x = 0
        delta_y = 0
        if(x_out > 0.7):
            delta_x = agent_size
        elif(x_out < 0.3):
            delta_x = -agent_size

        if (y_out > 0.7):
            delta_y = agent_size
        elif(y_out < 0.3):
            delta_y = -agent_size

        super().move(delta_x,delta_y)