import control as ctl
import numpy as np
import matplotlib.pyplot as plt

plt.grid()
ran = np.linspace(0, 10, 1000)
for k in np.arange(0.1, 50, 0.1):
    den=[1, 4, 11, (14+k), (10+k)]
    s = np.roots(den)
    plt.plot(np.real(s), np.imag(s),'b*')
    G = ctl.tf([k], den)
    print(G)
    #For Step Response 
#uncomment the below line
    # ran,dom = ctl.step_response(G,ran)
    # plt.plot(ran,dom)

    plt.pause(0.1)