import math

def bisectionFunc(x):
    return math.tan(x) + math.tanh(x)

def calculateBisection(a, b, err):
    step=1
    x0=a
    x1=b
    x2=0
    flag = True
    f0 = bisectionFunc(a)
    f1 = bisectionFunc(b)
    if(f0*f1 > 0.0):
        print("Incorrect Guesses and the solution doesnot lie between this")
    while flag:
        x2 = (x0+x1)/2
        f2 = bisectionFunc(x2)
        print('Iteration - %d, x2 = %0.8f and f(x2) = %0.8f' % (step, x2, f2))
        #means If  the solution converges
        if(f0*f2 < 0):
            x1 = x2
        else:
            x0=x2
        step+=1
        flag = abs(f2) > err
    print("Root is %0.8f", x2)
        
            
calculateBisection(2, 3, 0.0001)