import numpy as np
import matplotlib.pyplot as plt

def logisticMap(meu, xn):
    return meu*xn*(1-xn)

def bifurication(meu_start, meu_end, x_start, no_iter):
    #defining arrays 
    XN=[]
    MEU=[]
    #it outputs the meu from range start to end with 1000 divisions
    meu_range = np.linspace(meu_start, meu_end, 1000)
    #looping throughout the range of meu
    for meu in meu_range:
        xn = x_start
        #now looping inside for number of iterations we want to perform this
        for j in range(no_iter):
            XN.append(xn)
            MEU.append(meu)
            xn = logisticMap(meu, xn) 
          
    # plotting meu vs x 
    plt.plot(MEU, XN, ls='', marker=',', color='red')
    plt.ylim(0, 1)
    plt.xlim(meu_start, 4)
    plt.show()


bifurication(2.8, 4, 0.023, 100)