import control
import matplotlib.pyplot as plt
import numpy

x= numpy.arange(1, 200, 1)
num = [1, 2]
den = [1, -1, 0]

#Creating a transfer function G = num/den
G = control.tf(num,den) 
print(G)
w = numpy.logspace(-100,100,5000)
control.nyquist(G,w);
plt.grid(True)
plt.title('Nyquist Diagram')
plt.xlabel('Re(s)')
plt.ylabel('Im(s)')
plt.show()