#NAME=DIYA ROLL NO:21001003039

# to compute cosine of x
import numpy
import math
a=float(input('Enter the angle in degrees:'))
x=3.14159*a/180 #convert angle to radians
sum=1  # initialise value
term=-1
d=1
for i in range (1,9):  #i will have values as 1,2,3,4,5,6,7,8
    d=d*(2*i)*(2*i-1)
    sum=sum+term*(x**(2*i))/d
    term=-term
print('cos(',a,')=',sum)
s=math.cos(x)
print(s)