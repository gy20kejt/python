# -*- coding: utf-8 -*-
"""
Created on Mon Mar 22 18:28:46 2021

@author: katie
"""
import random
import operator
import matplotlib.pyplot
import time
`
#set up function to calculate distance between using pythagorean code
def distance_between(a, b):
        return (((a[0] - b[0])**2) + ((a[1] - b[1])**2))**0.5
"""
Calculates distance between two coordinates.

Parameters:
a (list): A set of coordinates
b (list): A set of coordinates

Returns:
Float: The distance between the two coordinates

"""



  
# set random seed so that the results are reproducible
#random.seed(0)

num_of_agents = 10
num_of_iterations = 100
agents = []

# Make the agents.
for i in range(num_of_agents):
    agents.append([random.randint(0,99),random.randint(0,99)])

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

# plot agents
matplotlib.pyplot.xlim(0, 99)
matplotlib.pyplot.ylim(0, 99)
for i in range(num_of_agents):
    matplotlib.pyplot.scatter(agents[i][1],agents[i][0])
matplotlib.pyplot.show()
#starts a timer
start = time.perf_counter()

#set up variables for min and max distance
maxd = distance_between(agents[0], agents[1])
mind = distance_between(agents[0], agents[1])
#calculate the distance betten all agents
for j in range(num_of_agents):
    #j+1 calculates the range of a triangle in a matrix(like spss does for 
    #coefficent outputs)
    for i in range(j + 1, num_of_agents):
        distance = distance_between(agents[j], agents[i])
        maxd = max(maxd, distance)
        mind = min(mind, distance)
        print("distance between agent", i, "and agent", j, "=", distance)
print("maximum distance", maxd)
print("minimum distance", mind)
#stops the timer
end = time.perf_counter()
# tells the time taken
print("time = " + str(end- start))

