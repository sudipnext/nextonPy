#import matplotlib.pyplot for the graph
import matplotlib.pyplot as plt
#import numpy for the arrays and math-on-array stuff
import numpy as np
#import Slider from matplotlib.widgets
from matplotlib.widgets import Slider
#defining the domain
x = np.arange(-5,5,0.1)
#f, the function
def f(x,a=1,b=1,c=1):
    return a*b*(x*1j)**c
#adjusting the main plot dimensions
plt.subplots_adjust(bottom=0.18, top=0.95)
#plot the actual graph with the label (and assigong them into variables)
real_part, = plt.plot(x,np.real(f(x*1j)), label='f(xj) real part')
imag_part, = plt.plot(x,np.imag(f(x*1j)), label='f(xj) imaginary part')
#show the label
plt.legend()
#making sliders
axSlider1 = plt.axes([0.1, 0.02, 0.8, 0.03])
Slider1 = Slider(axSlider1,"a",valmin=0,valmax=2,valinit=1, valstep=0.01,)

axSlider2 = plt.axes([0.1, 0.06, 0.8, 0.03])
Slider2 = Slider(axSlider2,"b",valmin=0,valmax=2,valinit=1, valstep=0.01,)

axSlider3 = plt.axes([0.1, 0.10, 0.8, 0.03])
Slider3 = Slider(axSlider3,"c",valmin=0,valmax=2,valinit=1, valstep=0.01,)
#the functions of how the value of the slider affect the graph
def A(aval):
    aval = Slider1.val
    real_part.set_ydata(np.real(f(x*1j,aval,Slider2.val,Slider3.val)))
    imag_part.set_ydata(np.imag(f(x*1j,aval,Slider2.val,Slider3.val)))
    plt.draw()
def B(bval):
    bval = Slider2.val
    real_part.set_ydata(np.real(f(x*1j,Slider1.val,bval,Slider3.val)))
    imag_part.set_ydata(np.imag(f(x*1j,Slider1.val,bval,Slider3.val)))    
    plt.draw()
def C(cval):
    cval = Slider3.val
    real_part.set_ydata(np.real(f(x*1j,Slider1.val,Slider2.val,cval)))
    imag_part.set_ydata(np.imag(f(x*1j,Slider1.val,Slider2.val,cval)))    
    plt.draw()
#applying those fucntions into sliders
Slider1.on_changed(A)
Slider2.on_changed(B)
Slider3.on_changed(C)
#show the graph
plt.show()