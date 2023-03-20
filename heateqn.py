import numpy as np
import matplotlib.pyplot as plt

#specifying range of x
# small change in position and time 
h=0.025
k=0.025
x= np.arange(0, 1+h, h)
t= np.arange(0,0.1+k, k)

#initialize a matrix which stores all the numbers
n=len(x)
m=len(t)
#T= temper vector
T=np.zeros((n, m))

#defining boundary condn
boundaryCondns =[0, 0]
#0 to all
T[0,:] = boundaryCondns[0]
T[-1, :] = boundaryCondns[1]

#initial condns
initialCondns = np.sin(np.pi*x)
#all rows but first
T[:, 0] = initialCondns
#here rows are defined as positions and columns as time in the matrix above
lamd = k/h**2
#outer loop time and inner loop position
#we know initial condns so we are starting at index 1
for j in range(1, m):
    for i in range(1, n-1):
        T[i, j] = lamd*T[i-1, j-1]+(1-2*lamd)*T[i, j-1] + lamd * T[i+1, j-1]

R= np.linspace(1, 0, m)
B= np.linspace(0, 1, m)
G =0
for j in range(m):
    plt.plot(x, T[:, j], color=[R[j], G, B[j]])
plt.legend(t)
plt.xlabel('distance [m]')
plt.ylabel('Temperature [degree C]')
plt.show()