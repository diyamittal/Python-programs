#NAME=DIYA ROLL NO:21001003039

# program to check if a year is leap or not  
import numpy
year=int(input('Enter the year:'))
while (year <= 0):
    print('Not a valid input')
    year=int(input('Re-Enter the year:'))
a=year % 4
b=year % 100
c=year % 400
if (a==0 and b!=0 or b==0 and c==0):
    print('year is leap')
else:
    print('year is not leap')
    