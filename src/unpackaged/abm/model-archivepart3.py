# -*- coding: utf-8 -*-
"""
Created on Mon Mar 22 18:28:46 2021

@author: katie
"""
import random
import operator
import matplotlib.pyplot

#def distance_between(agents_row_a, agents_row_b):
#        return (((agents_row_a[0] - agents_row_b[0])**2) +
#        ((agents_row_a[1] - agents_row_b[1])**2))**0.5
def distance_between(a, b):
    return (((a[0] - b[0])**2) + ((a[1] - b[1])**2))**0.5

# Set random seed so that the results are reproducible
#random.seed(0)
random.seed(1)

num_of_agents = 3
num_of_iterations = 2
agents = []

# Make the agents.
for i in range(num_of_agents):
    agents.append([random.randint(0,99),random.randint(0,99)])
agents.append([13, 14])
agents.append([10, 10])
print("num_of_agents", len(agents))
num_of_agents = len(agents)
print(agents)

# Calculate the maximum distance between all the agents
for j in range(0, num_of_agents, 1):
    print("j", j)
    for i in range(0, num_of_agents, 1):
        print("i", i)
        distance = distance_between(agents[j], agents[i])
        print("distance between agent", i, "and agent", j, "=", distance) 

# Move the agents.
for j in range(num_of_iterations):
    for i in range(num_of_agents):

        if random.random() < 0.5:
            agents[i][0] = (agents[i][0] + 1) % 100
        else:
            agents[i][0] = (agents[i][0] - 1) % 100

        if random.random() < 0.5:
            agents[i][1] = (agents[i][1] + 1) % 100
        else:
            agents[i][1] = (agents[i][1] - 1) % 100
print(agents)

# Plot agents
matplotlib.pyplot.xlim(0, 99)
matplotlib.pyplot.ylim(0, 99)
for i in range(num_of_agents):
    matplotlib.pyplot.scatter(agents[i][1],agents[i][0])
matplotlib.pyplot.show()

maxd = distance_between(agents[0], agents[1])
# Calculate the maximum distance between all the agents
for j in range(0, num_of_agents, 1):
    print("j", j)
    #for i in range(0, num_of_agents, 1):
    for i in range(j + 1, num_of_agents, 1):
        #if (i != j):
        #if (i < j):
            print("i", i)
            distance = distance_between(agents[j], agents[i])
            maxd = max(maxd, distance)
            print("distance between agent", i, "and agent", j, "=", distance)
print("maximum distance", maxd)
