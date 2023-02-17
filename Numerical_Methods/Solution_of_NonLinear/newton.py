import math

def fun(x):
    return x**3 - 5*x - 9

def derfun(x):
    return 3*x*x -5


def newtonCalc(a, err):
    step=1
    x1=a
    flag= True
    while flag:
        xn = x1-(fun(x1)/derfun(x1))
        x1=xn
        print('Iteration - %d, xn = %0.8f and f(xn) = %0.8f' % (step, xn, fun(xn)))
        flag = abs(fun(xn)) > err
        step +=1
    print("root is xn %0.6f",xn)

newtonCalc(2, 0.000001)