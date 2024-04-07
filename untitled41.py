#NAME=DIYA ROLL NO:21001003039

import math
def nthRoot(A,N):
        a=5.2 #initial approximation
        e=0.001 # tolerance allowed
        t = 5 #initial value of tolerance
    #  loop until we reach desired accuracy
        while t > e:
            b = a-(a**N - A)/(N*a**(N-1))
            t=abs(b**N-A)
            a=b
        return a
 
# Driver code
N = 4
A = 625
root = nthRoot(A, N)
print(N,'th root of',A,'is=',root)