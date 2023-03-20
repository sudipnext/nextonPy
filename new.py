import numpy as np
import matplotlib.pyplot as plt
from math import sin, pi, cos




x= np.arange(0, 4, 0.0001);
y=[]
print(x)
for i in range(len(x)):
    y1 = 1-(1/2)*x[i]**2+(1/24)*x[i]**4
    y.append(y1)
print(y)
plt.plot(x, y)
plt.show()