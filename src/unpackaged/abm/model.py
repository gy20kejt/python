# -*- coding: utf-8 -*-
"""
Created on Tue Apr 13 13:42:09 2021

@author: katie
"""


#Import Libraries

import random
import matplotlib
matplotlib.use('TkAgg') 
#import operator
import tkinter
import matplotlib.pyplot
import agentframework
import csv
import matplotlib.animation 
import requests
import bs4


# Web Scraping
page = requests.get('https://www.geog.leeds.ac.uk/courses/computing/practicals/python/agent-framework/part9/data.html')
content = page.text
soup = bs4.BeautifulSoup(content, 'html.parser')
tds_y = soup.find_all(attrs={"class" : "y"})
tds_x = soup.find_all(attrs={"class" : "x"})

print(tds_y)
print(tds_x)


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

fig = matplotlib.pyplot.figure(figsize=(7, 7))
ax = fig.add_axes([0, 0, 1, 1])


# Make the agents.  Include Environment and know other agents
for i in range(num_of_agents):
    y = int(tds_y[i].text)
    x = int(tds_x[i].text)
    agents.append(agentframework.Agent(environment, agents, y, x))

carry_on = True	

def update(frame_number):
    
    fig.clear()   
    global carry_on
    
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
    
    if random.random() < 0.1:
        carry_on = False
        print("stopping condition")
        
    for i in range(num_of_agents):
        matplotlib.pyplot.scatter(agents[i]._x,agents[i]._y)
       # print(agents[i]._x,agents[i]._y)

def gen_function(b = [0]):
    a = 0
    global carry_on #Not actually needed as we're not assigning, but clearer
    while (a < 10) & (carry_on) :
        yield a			# Returns control and waits next call.
        a = a + 1

       
#animation = matplotlib.animation.FuncAnimation(fig, update, interval=1, 
#repeat=False, frames=num_of_iterations)
                                    
#animation = matplotlib.animation.FuncAnimation(fig, update, 
                   #    frames=gen_function, repeat=False)
#matplotlib.pyplot.show()
# Create function to run the model
def run():
    animation = matplotlib.animation.FuncAnimation(fig, update,
    frames=gen_function, repeat=False)
    canvas.draw()
  

#Create  GUI      
root = tkinter.Tk()
root.wm_title("Model")
canvas = matplotlib.backends.backend_tkagg.FigureCanvasTkAgg(fig, master=root)
canvas._tkcanvas.pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1) 
menu_bar = tkinter.Menu(root)
root.config(menu=menu_bar)
model_menu = tkinter.Menu(menu_bar)
menu_bar.add_cascade(label="Model", menu=model_menu)
model_menu.add_command(label="Run model", command=run) 

tkinter.mainloop() 



