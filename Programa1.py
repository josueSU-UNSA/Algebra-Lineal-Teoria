
import numpy as np

def gaussEliminArray(a,b):
    n = len(b)
    n1=len(b[0,:])
    for k in range(0,n):    # k=0,...,n-1
        for i in range(k+1,n): # i=k+1
            if a[i,k] != 0.0:
                lam = a [i,k]/a[k,k]
                a[i,k+1:n] = a[i,k+1:n] - lam*a[k,k+1:n]
                for j in range(n1):
                    b[i,j]=b[i,j]-lam*b[k,j]
    for l in range(n1):
        for k in range(n-1,-1,-1):
            b[k,l] = (b[k,l] - np.dot(a[k,k+1:n],b[k,k+1:n]))/a[k,k]
    return (a,b)
print("Gauss eliminacion con matrices")
a=np.array([[6,-4,1],
           [-4,6,-4],
          [1,-4,6]],float)
b=np.array([[-14,36,6],[22,-18,7]],float)
print(gaussEliminArray(a,b)[1])
print(len(b[0,:]))
