from agent import *
from agent2 import *
import numpy as np

class LookUpTable():
    '''
    Note that the look up table is independent of input, 
    aslong as it is hashable. and therefore does not need to 
    be redefined per agent senses. 
    '''
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
    An agent which uses a LookUpTable as a brain 
    Inputs are RGB of the cell they are on. 
    Ouput is one of, Up, Down, Left or Right 
    '''
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


class RL_agent2(Agent):
    '''
    An agent which uses a LookUpTable as a brain 
    Inputs are RGB of the cell they are on. 
    Ouput is one of, Up, Down, Left or Right 
    '''

    def __init__(self,x,y,grid):
        super().__init__(x,y)
        self.type = "RL_2"
        self.c = (random.randint(0,255),random.randint(0,255),120)

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


        last_input = self.last_input
        # Get the cell we are standing on
        c = grid.get_cell(self.x,self.y)
        self.last_input = (c.r, c.g, c.b)
        # 255^3 * 255^3 * 4 = 1.099768e+15
        sense = (self.last_action, last_input, self.last_input)
        # Ask our brain what to do given our new input
        self.last_action = self.brain.predict(sense)
        
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


class RandomisedLookUpTable(LookUpTable):
    '''
    The look up table will always do what it thinks it should
    It needs to explore other options than the first one given to it
    Enter the explore vs exploit question.
    '''
    def __init__(self):
        super().__init__()

    def predict(self,x):
        r = random.random()

        if (r < 0.02):
            return random.choice(self.actions)
        else:
            return super().predict(x)

class RRL_agent(RL_agent):
    def __init__(self,x,y,grid):
        super().__init__(x,y,grid)
        self.type = "RRL"
        self.c = (random.randint(0,255),random.randint(0,255),255)

        # Make our look up table brain
        self.brain = RandomisedLookUpTable()

        # Get an inital input
        c = grid.get_cell(self.x,self.y)
        senses = (c.r, c.g, c.b)
        self.last_input = senses
        self.last_action = "up"

class R_LookUpTable():
    '''
    Note that the look up table is independent of input, 
    aslong as it is hashable. and therefore does not need to 
    be redefined per agent senses. 
    '''
    def __init__(self):
        self.memory = {} # (0,0,255) : [0,0,10]
        self.actions = ["left", "right", "forward"]
        self.inv_actions = {"left":0, "right":1, "forward":2}

    def predict(self,x):
        if x in self.memory:
            r = random.random()
            if (r < 0.05): return random.choice(self.actions)

            # Look up the stimulus in our memory
            memory_of_stimulus = self.memory[x]

            # Pick the best action we know
            action_index = np.argmax(memory_of_stimulus)
            return self.actions[action_index]
        else:
            # We havent seen this input before, pick random
                        # left, right, up, down
            self.memory[x] = [0,     0,     1]

            r = random.random()
            if (r < 0.10):
                return "left"
            elif (r < 0.20):
                return "right"
            else:
                return "forward"

    def update(self,last_input, last_action, reward):
        # Turn "right" into 1
        action_num = self.inv_actions[last_action]


        if last_input in self.memory:
            # We have seen it before, update our score
            self.memory[last_input][action_num] += reward
        else:
            # We have not seen it before
            new_memory = [0,0,0]
            new_memory[action_num] = reward
            self.memory[last_input] = new_memory

    def __repr__(self):
        return str(self.memory)

class RL_agentRot(Agent2):
    '''
    An agent which uses a LookUpTable as a brain 
    Inputs are RGB of the cell they are on. 
    Ouput is one of, Up, Down, Left or Right 
    '''
    def __init__(self,x,y,grid):
        super().__init__(x,y)
        self.type = "RL Agent Rot"
        self.c = (random.randint(0,255),random.randint(0,255),255)

        # Make our look up table brain
        self.brain = R_LookUpTable()

        # Get an inital input
        c = grid.get_cell(self.x,self.y)
        c_n = grid.get_cell(self.infront_x,self.infront_y)
        senses = (self.degrees, c.r, c.g, c.b, c_n.r, c_n.g, c_n.b)
        self.last_input = senses
        self.last_action = "forward"

    def live(self, grid, reward):
        # Update our look up table based on the last reward
        self.brain.update(self.last_input, self.last_action, reward)
        self.life += 10

        # Get our new input 
        c = grid.get_cell(self.x,self.y)
        c_n = grid.get_cell(self.infront_x,self.infront_y)
        self.last_input = (self.degrees, c.r, c.g, c.b, c_n.r, c_n.g, c_n.b)
        print("Input: ", self.degrees, "C:", c.type, "C-n", c_n.type)
        print(self.brain)
        # Ask our brain what to do given our new input
        self.last_action = self.brain.predict(self.last_input)
        print("Output: ", self.last_action)

        super().move(self.last_action)