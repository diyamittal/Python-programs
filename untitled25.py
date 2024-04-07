#NAME=DIYA ROLL NO:21001003039

# program for hcf of three numbers
# function for HCF of two numbers
def hcf(a,b):
    if a > b:
        dvd=a
        dvsor=b
    else:
        dvd=b
        dvsor=a
    r=dvd % dvsor
    while (r !=0):
        dvd=dvsor
        dvsor=r
        r=dvd % dvsor
    hcf=dvsor
    return hcf
# main program
m=int(input('Enter first number:'))
n=int(input('Enter second number:'))
p=int(input('Enter third number:'))
while ( m<= 0 or n<= 0 or p <= 0):
    print('invalid data')
    m=int(input('Enter first number:'))
    n=int(input('Enter second number:'))
    p=int(input('Enter third number:'))
u=hcf(hcf(m,n),p)
print(u)