# -*- coding: utf-8 -*-
"""
Created on Tue Apr 13 13:44:51 2021

@author: katie
"""

# import required modules
import random

# Create the agent class
class Agent:
    def __init__(self, environment, agents):
        self._y = random.randint(0,99)
        self._x = random.randint(0,99)
        self.environment = environment
        self.agents = agents
        self.store = 0 
        
 # setting set and get to protect x and y variables   
   
    def x(self):
        return self._x
    
    def getx(self):
        return self._x

    def setx(self, value):
        self._x = value

    def y(self):
        return self._y

    def gety(self):
        return self._y

    def sety(self, value):
        self._y = value    
 
    
 # defines how to make the agents move(% 100 is to make it torus)    
    def move(self):
        if random.random() < 0.5:
            self._y = (self._y + 1) % 100
        else:
            self._y = (self._y - 1) % 100

        if random.random() < 0.5:
            self._x = (self._x + 1) % 100
        else:
            self._x = (self._x - 1) % 100
            
  # defines how an agent eats
          
    def eat(self): # can you make it eat what is left?
        if self.environment[self._y][self._x] > 10:
            self.environment[self._y][self._x] -= 10
            self.store += 10 
            
# defines function to share with neighbour

    def share_with_neighbours(self, neighbourhood):
        random.shuffle(self.agents)
        for agent in self.agents:
            distance = self.distance_between(agent)
            if distance <= neighbourhood:
                addup = self.store + agent.store
                aver = addup / 2
                self.store = aver
                agent.store = aver
                print("sharing " + str(distance) + " " + str(aver))
                
# caculate the distance between the agents              
    def distance_between(self, agent):
        return (((self._x - agent._x)**2) + ((self._y - agent._y)**2))**0.5