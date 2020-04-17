from agent import *
import settings
import numpy as np

square_size = settings.square_size
agent_size = square_size

class Agent2(Agent):
    def __init__(self,x,y):
        super().__init__(x,y)
        self.type = "Agent2"
        self.actions = ["left", "right", "forward"]
        self.degrees = 0

    def live(self, grid, reward):
        action = random.choice(self.actions)
        self.move(action)

    def move(self, action):
        if (action == "right"):
            self.degrees = (self.degrees + 90) % 360
        elif (action == "left"):
            self.degrees = (self.degrees - 90) % 360
        elif (action == "forward"):
            if (self.degrees == 0):
                # Move up
                self.y += agent_size
            elif (self.degrees == 90):
                # Move right
                self.x += agent_size
            elif (self.degrees == 180):
                # Move down
                self.y -= agent_size
            elif (self.degrees == 270):
                # Move left
                self.x -= agent_size

        # Sanity checks
        if(self.x <= 0):
            self.x = w_width - agent_size
        if(self.y <= 0):
            self.y = w_height - agent_size
        if (self.x + agent_size > w_width):
            self.x = 0
        if (self.y + agent_size > w_height):
            self.y = 0

    def draw(self,screen):
        # Rotate the end point 
        end_point = np.array([self.x ,self.y])
        r = np.array([[0,-1],
                      [1, 0]])
        n = np.array([0,10])
        for i in range(4-self.degrees//90):
            n = np.dot(r,n)
        end_point += n
        pygame.draw.line(screen, (255,255,255), [self.x, self.y], end_point.tolist())
        pygame.draw.circle(screen, self.c, (self.x, self.y), agent_size//2)
