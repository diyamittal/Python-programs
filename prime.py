import math
n=int(input('Enter the number :'))
while (n <= 0): 
    print('Not a valid input')
    n=int(input('Re-enter the number :'))
if (n==1):
    print('1 is neither prime or nor composit')
else:
    k=math.floor((math.sqrt(n)))  # divisors
    remd=1
    i=2
    while (i <= k and remd !=0):
        remd=n % i
        i=i+1
    if(remd==0):
        print('number is not prime')
    else:
        print('number is prime')
