import control as ctl
import numpy as np
import matplotlib.pyplot as plt

for kp in range(0,100):
    den=[1, 8, 36, 80, kp]
    s = np.roots(den)
    plt.plot(np.real(s), np.imag(s),'b*')
    print(kp)
    G = ctl.tf([kp], den)
    print(G)
    plt.pause(0.1)