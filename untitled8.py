#NAME=DIYA ROLL NO:21001003039

# to compute sine of x
import numpy
import math
a=float(input('Enter the angle in degrees:'))
x=3.14159*a/180
sum=x
term=-1
d=1
for i in range (1,9):
    d=d*(2*i+1)*(2*i)
    sum=sum+term*(x**(2*i+1))/d
    term=-term
print('sin(',a,')=',sum) 
s=math.sin(x)
print(s)
