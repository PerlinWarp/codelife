from agent import *
from agent2 import *
import numpy as np
import matplotlib.pyplot as plt


class Q_Table():
    '''
    Note that the look up table is independent of input, 
    aslong as it is hashable. and therefore does not need to 
    be redefined per agent senses. 
    '''
    def __init__(self, lr=0.05, e=0.25, d=0.5):
        self.q_table = {} # (0,0,255) : [0,0,10]
        self.actions = ["left", "right", "forward"]
        self.inv_actions = {"left":0, "right":1, "forward":2}

        # Hyper Parameters
        self.learning_rate = lr
        self.epsilon = e
        self.discount = d

    def predict(self,state,life):
        if state in self.q_table and life/100 > self.epsilon:
            return np.argmax(self.q_table[state])
        else:
            return random.choice(self.actions)


    def update(self, last_state, last_action, new_state, reward):
        # Turn "right" into 1
        action_num = self.inv_actions[last_action]

        if new_state in self.q_table:
            max_future_q = np.max(self.q_table[new_state]) 
        else: max_future_q = 0

        if last_state in self.q_table:
            # We have seen it before, update our score
            current_q = q_table[last_state][last_action]
            new_q = (1 - self.learning_rate) * current_q + self.learning_rate*(reward + self.discount * max_future_q)
            self.memory[last_input][action_num] += new_q

    def __repr__(self):
        return str(self.q_table)

class Q_agent(Agent2):
    '''
    An agent which uses a LookUpTable as a brain 
    Inputs are RGB of the cell they are on. 
    Ouput is one of, Up, Down, Left or Right 
    '''
    def __init__(self,x,y,grid,brain=None):
        super().__init__(x,y)
        self.type = "Q Agent"
        self.c = (random.randint(0,255),random.randint(0,255),255)

        # Make our look up table brain
        if (brain):
            self.brain = brain
        else:
            self.brain = Q_Table()


        # Get an inital input
        c = grid.get_cell(self.x,self.y)
        c_n = grid.get_cell(self.infront_x,self.infront_y)
        senses = (self.degrees, c.r, c.g, c.b, c_n.r, c_n.g, c_n.b)
        self.input = senses
        self.last_action = "forward"

    def live(self, grid, reward):
        last_input = self.input
        # Get our new input 
        c = grid.get_cell(self.x,self.y)
        c_n = grid.get_cell(self.infront_x,self.infront_y)
        self.input = (self.degrees, c.r, c.g, c.b, c_n.r, c_n.g, c_n.b)

        # Update our look up table based on the last reward
       #update(last_state, last_action, new_state, reward):
        self.brain.update(last_input, self.last_action,self.input, reward)

        #print("Input: ", self.degrees, "C:", c.type, "C-n", c_n.type)
        #print(self.brain)
        # Ask our brain what to do given our new input
        self.last_action = self.brain.predict(self.input, self.life)
        #print("Output: ", self.last_action)

        super().move(self.last_action)


class Population():
    def __init__(self, size, grid, screen):
        self.size = size
        self.grid = grid
        self.screen = screen
        self.agents = []
        self.dead_agents = []
        self.dead_scores = []
        for s in range(size):
            x = random.randint(0,w_width-100)
            y = random.randint(0,w_height-100)
            lr = random.random()
            e = random.random()
            d = random.random()
            baby_brain = Q_Table(lr, e, d)
            self.agents.append(Q_agent(x,y,grid,brain=baby_brain))

        # Metrics
        self.lives = []
        self.gens = [[],[],[]]

    def cross_over(self,a,b):
        # Combine the parameters of a and b 
        f = random.random()
        lr = (a.learning_rate*f + b.learning_rate*(1-f))/2
        f = random.random()
        e = (a.epsilon*f + b.epsilon*(1-f))/2
        f = random.random()
        d = (a.discount*f + b.discount*(1-f))/2

        # Mutation
        if (random.random() < 0.02):
            lr = lr * 1.2
        elif(random.random() < 0.04):
            lr = lr * 0.8
        if (random.random() < 0.02):
            d = d * 1.2
        elif (random.random() < 0.04):
            d = d * 0.8
        if (random.random() < 0.04):
            e = random.random()

        baby_brain = Q_Table(lr, e, d)
        return baby_brain

    def breed(self):
        # Returns a new population
        babies = []
        # sum(self.dead_scores) should be zero for a prob dist
        self.dead_scores = np.array(self.dead_scores)/sum(self.dead_scores)
        for i in range(self.size):
            mum, dad = np.random.choice(self.dead_agents, 2, p=self.dead_scores)
            x = random.randint(0,w_width-100)
            y = random.randint(0,w_height-100)
            newborn_brain = self.cross_over(mum.brain, dad.brain)
            baby = Q_agent(x,y,self.grid,brain=newborn_brain)
            babies.append(baby)
        return babies

    def run(self):
        if (len(self.agents) > 0):
            for agent in self.agents:
                if (agent.life < 1):
                        self.dead_agents.append(agent)
                        self.dead_scores.append(agent.alive_time)
                        print(len(self.agents)-1,"still alive")
                        self.agents.remove(agent)
                        del agent
                else:
                    agent.run(self.grid)
                    agent.draw(self.screen)
        else:
            # Breed em
            print("New Population")
            ma = max(self.dead_scores)
            mi = min(self.dead_scores)
            av = np.average(self.dead_scores)

            print("Max Life: ",ma)
            print("Min Life: ",mi)
            print("Avg Life: ",av)
            try:
                print("lr", self.dead_agents[self.size-1].brain.learning_rate)
                print("d", self.dead_agents[self.size-1].brain.discount)
                print("e", self.dead_agents[self.size-1].brain.epsilon)
            except:
                raise ValueError(self.size, len(self.dead_agents))

            self.gens[0].append(ma)
            self.gens[1].append(mi)
            self.gens[2].append(av)

            babies = self.breed()
            self.agents = babies

            self.dead_agents = []
            self.dead_scores = []
            self.lives = []

    def stats(self):
        gens = range(len(self.gens[0]))
        maxs = self.gens[0]
        mins = self.gens[1]
        avgs = self.gens[2]

        plt.plot(gens, maxs)
        plt.plot(gens, mins)
        plt.plot(gens, avgs)
        plt.legend(['Max Life', 'Min Life', 'Avg Life'], loc='upper left')
        plt.show()



