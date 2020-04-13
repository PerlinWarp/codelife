from agent import *
import numpy as np

# Helper functions 
get_bin = lambda x, n: format(a, 'b').zfill(8)

class LookUpTable():
    def __init__(self):
        self.memory = {} # (0,0,255) : [0,0,0,10]
        self.actions = ["left", "right", "up", "down"]
        self.inv_actions = {"left":0, "right":1, "up":2, "down":3}

    def predict(self,x):
        if x in self.memory:
            # Look up the stimulus in our memory
            memory_of_stimulus = self.memory[x]

            # Pick the best action we know
            action_index = np.argmax(memory_of_stimulus)
            return self.actions[action_index]
        else:
            # We havent seen this input before, pick random
                        # left, right, up, down
            self.memory[x] = [0,     0,     0,    0]

            r = random.random()
            if (r < 0.25):
                return "left"
            elif (r < 0.5):
                return "right"
            elif (r < 0.75):
                return "up"
            else:
                return "down"

    def update(self,last_input, last_action, reward):
        # Turn "right" into 1
        action_num = self.inv_actions[last_action]


        if last_input in self.memory:
            # We have seen it before, update our score
            self.memory[last_input][action_num] += reward
        else:
            # We have not seen it before
            new_memory = [0,0,0,0]
            new_memory[action_num] = reward
            self.memory[last_input] = new_memory


class RL_agent(Agent):
    '''
    An agent which uses a perceptron as a brain 
    Inputs are green pixel
    Ouput is x and y movements being either forward or backwards
    '''
    input_size = 1
    hidden_layer_size = 1

    def __init__(self,x,y,grid):
        super().__init__(x,y)
        self.type = "RL"
        self.c = (random.randint(0,255),random.randint(0,255),255)

        # Make our look up table brain
        self.brain = LookUpTable()

        # Get an inital input
        c = grid.get_cell(self.x,self.y)
        senses = (c.r, c.g, c.b)
        self.last_input = senses
        self.last_action = "up"

    def live(self, grid, reward):
        # Update our look up table based on the last reward
        self.brain.update(self.last_input, self.last_action, reward)


        # Get our new input 
        c = grid.get_cell(self.x,self.y)
        self.last_input = (c.r, c.g, c.b)

        # Ask our brain what to do given our new input
        self.last_action = self.brain.predict(self.last_input)
        
        # Prediction
        self.delta_x = 0
        self.delta_y = 0
        if(self.last_action == "right"):
            self.delta_x = agent_size
        elif(self.last_action == "left"):
            self.delta_x = -agent_size
        elif(self.last_action == "up"):
            self.delta_y = agent_size
        elif(self.last_action == "down"):
            self.delta_y = -agent_size
        else:
            raise ValueError("Invalid output")

        super().move(self.delta_x,self.delta_y)