# -*- coding: utf-8 -*-
"""
Created on Mon Mar 22 18:28:46 2021

@author: katie
"""
# import library
import random
import operator
import matplotlib.pyplot


num_of_agents = 10 
num_of_iterations = 100
# create empty list called agents
agents = []

# Set up Variables(y,x) on random 100x100 grid. as many as num of agents
for i in range(num_of_agents):
    agents.append([random.randint(0, 99),random.randint(0, 99)])

# Random walk one step number of iteration times for each agent. It will be in a torus so no points disapear

for j in range(num_of_iterations):
    for i in range(num_of_agents):
        if random.random() < 0.5:
            agents[i][0] = (agents[i][0] +1) % 100
        else:
            agents[i][0] = (agents[i][0] -1) % 100
    
        if random.random() < 0.5:
            agents[i][1] = (agents[i][1] +1) % 100
        else:
            agents[i][1] = (agents[i][1] -1) % 100
 

print(agents)    

# simplified (((y0 - y1)**2) + ((x0 - x1)**2))**0.5
#y_diff = (agents[0][0] - agents[1][0])
#y_diffsq = y_diff * y_diff
#x_diff = (agents[0][1] - agents[1][1])
#x_diffsq = x_diff * x_diff
#sum = y_diffsq + x_diffsq
#answer = sum**0.5
#print(answer)

# find out which is most east (highest x number)
print(max(agents, key=operator.itemgetter(1)))

matplotlib.pyplot.ylim(0, 99)
matplotlib.pyplot.xlim(0, 99)
for i in range(num_of_agents):
    matplotlib.pyplot.scatter(agents[i][1],agents[i][0])
#create a new variable for east most
m = max(agents, key=operator.itemgetter(1))
matplotlib.pyplot.scatter(m[1], m[0], color='red')
matplotlib.pyplot.show()