import control as ctl
import numpy as np
import matplotlib.pyplot as plt

plt.grid()
ran = np.linspace(0, 10, 1000)
for k in np.arange(1, 300, 1):
    den=[1, 9, 72, (64+k), (2*k)] 
    s = np.roots(den)
    plt.plot(np.real(s), np.imag(s),'b*')
    plt.title("Root Locus Plot")
    plt.xlabel("Sigma")
    plt.ylabel("jw")
    G = ctl.tf([k], den)
    print(G)
    #For Step Response 
#uncomment the below line
    # ran,dom = ctl.step_response(G,ran)
    # plt.plot(ran,dom)

    plt.pause(0.1)