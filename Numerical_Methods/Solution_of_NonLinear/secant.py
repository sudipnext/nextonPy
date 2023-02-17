import math

def fun(x):
    return x*x-2

def secantCalcuator(a, b, err):
    step=1
    x0=a
    x1=b
    f0= fun(a)
    f1 = fun(b)
    flag=True
    if(f0*f1 >0):
        print("The solution between these point is not converging")
    while flag:
        x2 = (f1*x0 - f0*x1)/(f1-f0)
        f2=fun(x2)
        print('Iteration - %d, x2 = %0.8f and f(x2) = %0.8f' % (step, x2, f2))
        #now again checking whether the solution is converging or not
        if(f0*f2 < 0):
            x1=x2
        else:
            x0=x2
        step+=1
        flag = abs(f2) > err
    print("The root is %0.6f", x2)

secantCalcuator(1, 2, 0.001)