#Importing Necessary libraries
import matplotlib.pyplot as plt
import math
import numpy as np
from itertools import product

#defining functions and it's derivatives
def f(z):
    return z**3 -1
def df(z):
    return 3*z**2
#writing necessary things
#defining error
err = 0.01
maxSample=1000
#no of iterations
niter= 1000
#array of roots
roots_fun = [complex(1, 0), complex(-1/2, math.sqrt(3)/2), complex(-1/2, -math.sqrt(3)/2)]
#array of colors most preferably red for the first root blue for the second one and green for the third one
COLORS = ['red', 'blue', 'green']
#creating an object for holding the assumed random roots which falls between the required err neglence
points = {}
for root in roots_fun:
    points[root]=[]
#Newton method 
def newtonCalc(z):
    step =0
    flag = True
    while flag:
        z = z -(f(z)/df(z))
        step+=1
        flag = abs(f(z)) > err
    return z

#Adding points nearest to the roots
def adding_points(x, y):
    root = newtonCalc(complex(x, y))
    for r in roots_fun:
        if abs(r-root) < err:
            points[r].append((x, y))

#plotting the points now
def newtonFractalPlot():
    #creating complex number ranges
    for (x,y) in product(np.linspace(-1, 1, maxSample), np.linspace(-1, 1, maxSample)):
        adding_points(x, y)
    for i, r in enumerate(roots_fun):
        plt.scatter(*zip(*points[r]), 
                    color=COLORS[i], 
                    s=0.01)
        plt.title("f(x)=Z**3-1")

    plt.show()
newtonFractalPlot()

