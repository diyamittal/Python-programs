#NAME=DIYA ROLL NO:21001003039

# program for roots of quadratic equation  
import numpy
import math
a=float(input('Enter the coeff. of x^2:'))
b=float(input('Enter the coeff. of x:'))
c=float(input('Enter constant term:'))
while (a==0):
    print('Not a valid input')
    a=input('Re-Enter the coeff. of x^2:')
disc=b**2-4*a*c
if (disc >= 0):
    r1=(-b+math.sqrt(disc))/(2*a)
    r2=(-b-math.sqrt(disc))/(2*a)
    print('root1=',r1)
    print('root2=',r2)
else:
    real=-b/(2*a)
    imag=math.sqrt(-disc)/(2*a)
    print('root1=',real,'+i',imag)
    print('root2=',real,'-i',imag)