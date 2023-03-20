"""
d2u/dt^2 = c^2 d2u/dx^2
Solution by Finite Difference Method
"""
import numpy as np
from math import pi, sin
import matplotlib.pyplot as plt
#initial values
dx = 0.05
dt = 0.05
L=1
r=1*dt/dx #T/meu = 1

x=np.arange(0, L, dx)

pos_old =[]
pos_now=[]
pos_new=[]
A = 0.1 # amplitude

for i in range(len(x)):
    pos_old = pos_old +[A*sin(pi*x[i])]
    pos_new = pos_new +[A*sin(pi*x[i])]
    pos_now = pos_now +[A*sin(pi*x[i])]

# plt.xlabel("x")
# plt.ylabel("y")
# plt.plot(x, pos_now)
# plt.show()
t=0
while t< 1:
    
    fdata=[]
    for i in range(1, len(x)-1):
        pos_new[i] = r**2*(pos_now[i+1]+pos_now[i-1]-2*pos_now[i])+ 2*pos_now[i]-pos_old[i]
    for i in range(1, len(x)-1):
        pos_old = pos_now[i]
    for i in range(1, len(x)-1):
        pos_now[i] = pos_new[i]
    plt.plot(x, pos_new)
    plt.show()
    
    t = t+dt
