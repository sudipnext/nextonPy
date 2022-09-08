import control
import matplotlib.pyplot as plt
import numpy

num = [4, 1]
den = [2, 3, 1, 0, 0]

#Creating a transfer function G = num/den
G = control.tf(num,den) 
print(G)
w = numpy.logspace(-3,3,5000)
control.nyquist(G,w);
plt.grid(True)
plt.title('Nyquist Diagram')
plt.xlabel('Re(s)')
plt.ylabel('Im(s)')
plt.show()