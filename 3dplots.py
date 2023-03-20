import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d

#scatter plot 
# ax = plt.axes(projection="3d")
# ax.scatter(3, 4, 6)
# plt.show()

ax = plt.axes(projection="3d")

# x_data = np.random.randint(0, 100, (500,))
# y_data = np.random.randint(0, 100, (500,))
# z_data = np.random.randint(0, 100, (500,))


# ax.scatter(x_data, y_data, z_data, marker="x", alpha=0.7)
# plt.show()

# plotting functions
x_data = np.arange(-5,5, 0.1)
y_data = np.arange(-5, 5, 0.1)
# z_data = np.sin(x_data)* np.cos(y_data)


# ax.plot(x_data, y_data, z_data)
# plt.show()

#surface plots
X, Y = np.meshgrid(x_data, y_data)
z= np.sin(X)*np.cos(Y)
ax.plot_surface(X, Y, z, cmap="plasma")
plt.show()