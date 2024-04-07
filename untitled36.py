#NAME=DIYA ROLL NO:21001003039

# Magic square of any dimension
def magic_odd(d):
    return print('odd type magic sqaure created')      
def magic_4n(d):
    return print('4n type magic sqaure created')  
def magic_4n2(d):
    return print('4n+2 type magic sqaure created')
# main or calling program
n=int(input('Enter the dimension of required magic square:'))
if n<=0:
    print('invalid entry')
    n=int(input('Re-Enter the dimension:'))
if n %2 ==1: #if dimension is odd
    magic_odd(n)
else:
    if n%4==0:   # dimension is 4n type
        magic_4n(n)
    else:       # dimension is 4n+2 type
        magic_4n2(n)



    