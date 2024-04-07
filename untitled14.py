#NAME=DIYA ROLL NO:21001003039

# integration using trapezoidal rule
import math
def f(x):
    return x**2  #function to be integrated
a=float(input('Enter lower limit:'))
b=float(input('Enter upper limit:'))
n=10000 # number of intervals
h=(b-a)/n
sum=0 #initialise integral value
for i in range (n+1):
    sum=sum+f(a+i*h)
sum=h*(sum-(f(a)+f(b))/2)    
print(sum)
