#NAME=DIYA ROLL NO:21001003039

# program to compute hcf and lcm of 2 numbers  
import numpy
a=int(input('Enter first number :'))
b=int(input('Enter second number :'))
while (a <= 0 or b <=0):
    print('Not a valid input')
    a=int(input('Enter first number :'))
    b=int(input('Enter second number :'))
if ( a > b):
    dvd=a
    dvsor=b
else:
    dvd=b
    dvsor=a
remd=dvd % dvsor
while (remd !=0):
    dvd=dvsor
    dvsor=remd
    remd=dvd % dvsor
hcf=dvsor
print ('hcf=',hcf)
lcm=a*b/hcf
print('lcm=',lcm)
