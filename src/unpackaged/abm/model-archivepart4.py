# -*- coding: utf-8 -*-
"""
Created on Tue Apr 13 13:42:09 2021
@author: katie
"""

#import random
#import operator
import matplotlib.pyplot
import agentframework
import csv


#create environment by reading data from text file
f = open('in.txt', newline='') 
reader = csv.reader(f, quoting=csv.QUOTE_NONNUMERIC)
environment = []

for row in reader:		
    rowlist = []   		
    for value in row:				
        rowlist.append(value)
    environment.append(rowlist) 
f.close() 


num_of_agents = 10
num_of_iterations = 100
neighbourhood = 20
agents = []

# Make the agents.  Include Environment and know other agents
for i in range(num_of_agents):
    agents.append(agentframework.Agent(environment, agents))

# Makes the agents do things
for j in range(num_of_iterations):
    for i in range(num_of_agents):
        agents[i].move()
        agents[i].eat()
        agents[i].share_with_neighbours(neighbourhood)

#plotting envionrment and agents on map
matplotlib.pyplot.xlim(0, 99)
matplotlib.pyplot.ylim(0, 99)
matplotlib.pyplot.imshow(environment)
for i in range(num_of_agents):
    matplotlib.pyplot.scatter(agents[i]._x, agents[i]._y)
matplotlib.pyplot.show()