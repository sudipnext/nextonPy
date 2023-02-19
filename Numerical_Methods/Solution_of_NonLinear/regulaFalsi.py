def f(x):
    return x**3-2*x-5

def regulaFalsi(x1, x2, err):
    pos=1
    fx1= f(x1)
    fx2 = f(x2)
    if fx1 * fx2 > 0:
        print("The solutions doesn't lies between this interval")
    condn = True
    while condn:
        x3 = x1-(x2-x1)/(f(x2)-f(x1))*f(x1)
        print('Step- %d, x3 = %0.6f and f(x3) = %0.6f' % (pos, x3, f(x3)))
        if f(x3)*f(x1) < 0:
            x2= x3
        else:
            x1= x3
        condn = abs(f(x3)) > err
    print('\nRequired root is: %0.8f' % x3)


regulaFalsi(2, 3, 0.001)