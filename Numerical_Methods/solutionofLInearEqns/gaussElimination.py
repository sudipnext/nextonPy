import numpy as np


a = np.array([[3, -2, 5, 0],
             [4, 5, 8, 1],
             [1, 1, 2, 1],
             [2, 7, 6, 5]], float)
b= np.array([2, 4, 5, 7], float)
n= len(b)
x= np.zeros(n, float)
print(x)
#Elimination Stage
for i in range(n-1):
    for j in range(i+1, n):
        if a[j][i]== 0: continue
        factor = a[i][i]/a[j][i]
        for k in range(i, n):
            a[j][k] = a[i][k] - a[j][k]*factor
        b[j]= b[i]-b[j]*factor

#Back Substitution
x[n-1] = b[n-1] / a[n-1][n-1]
for i in range(n-2, -1, -1):
    sum =0
    for j in range(i+1, n):
        sum+=a[i][j]*x[j]
    x[i] = (b[i] - sum)/a[i][i]

print(a)
print(b)
print("the solution is ", x)