#NAME=DIYA ROLL NO:21001003039

# HCF and LCM  of two numbers
a=int(input('Enter first number:'))
b=int(input('Enter second number:'))
while ( a<= 0 or b<= 0):
    print('invalid data, the numbers have to be positive integers')
    a=int(input('Re-Enter first number:'))
    b=int(input('Re-Enter second number:'))
if a > b:
    dvd=a  # a is dividend
    dvsor=b #b is divisor
else:
    dvd=b
    dvsor=a
r=dvd % dvsor
while (r !=0):
    dvd=dvsor
    dvsor=r
    r=dvd % dvsor
hcf=dvsor
print('hcf(',a,',',b,')=',hcf)
lcm=a*b//hcf
print('lcm(',a,',',b,')=',lcm)
