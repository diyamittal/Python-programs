#NAME=DIYA ROLL NO:21001003039

#DESCRIPTION Write a program to find roots of a qaudratic equation
'''import math
a=float(input("Enter first coefficient"))
b=float(input("Enter second coefficient"))
c=float(input("Enter third coefficient"))
if(a==0):
    print("First cofficient should not be 0")
d=b*b-4*a*c
if(d>=0):
        r1=(-b+math.sqrt(d))/(2*a)
        r2=(-b-math.sqrt(d))/(2*a)
        print("Root 1 =",r1)
        print("Root 2 =",r2)
else:
    d=-d
    real=-b/(2*a)
    img=math.sqrt(d)/(2*a)
    print("Root 1 =",real,"+","i",img)
    print("Root2 = ",real,"-","i",img)'''
    
#DESCRIPTION Write a program to read a date and print next date
dd=int(input("Enter date"))
mm=int(input("Enter month"))
yy=int(input("Enter year"))
if(yy%100==0 and yy%400==0 or yy%100!=0 and yy%4==0):
    list1=[31,29,31,30,31,30,30,31,30,31,30,31]
else:
    list1=[31,28,31,30,31,30,30,31,30,31,30,31]
if(dd==list1[mm-1] and mm!=12):
    dd=1
    mm=mm+1
elif(dd==31 and mm==12):
    dd=1
    mm=1
    yy=yy+1
else:
    dd=dd+1
print(dd,"/",mm,"/",yy)

#DESCRIPTION Write a program to read a date and print previous date
'''dd=int(input("Enter date"))
mm=int(input("Enter month"))
yy=int(input("Enter year"))
if(yy%100==0 and yy%400==0 or yy%100!=0 and yy%4==0):
    list1=[31,29,31,30,31,30,30,31,30,31,30,31]
else:
    list1=[31,28,31,30,31,30,30,31,30,31,30,31]
if(dd==1 and mm!=1):
    mm=mm-1
    dd=list1[mm-1]
elif(dd==1 and mm==1):
    dd=1
    mm=1
    yy=yy-1
else:
    dd=dd-1
print(dd,"/",mm,"/",yy)'''

#DESCRIPTION Write a program to read two positive integers M N and to print all odd numbers
#between them(both M and N excluded)
'''a=int(input("Enter first number"))
b=int(input("Enter second number"))
print("Odd number between",a,"and",b,"are")
for i in range(a+1,b):
    if(i%2!=0):
        print(i)'''

#DESCRIPTION Write a program to read two positive integers M N and to print all even numbers
#between them(both M and N excluded)
'''a=int(input("Enter first number"))
b=int(input("Enter second number"))
print("Even numbers between",a,"and",b,"are")
for i in range(a+1,b):
    if(i%2==0):
        print(i)'''
        
#DESCRIPTION Write a program to read an integer number and print its reverse
'''n=int(input("Enter any number"))
sum=0
while(n!=0):
    r=n%10
    sum=sum*10 + r
    n=n//10
print("reverse of number is",sum)'''

#DESCRIPTION Write a program to read an integer number and to print
#Product of digits if it is odd
#Sum of its digits if it is even
'''n=int(input("Enter any number"))
sum=0
product=1
if(n%2==0):
    while(n!=0):
        r=n%10
        sum=sum + r
        n=n//10
    print("sum of digits is",sum)
else:
    while(n!=0):
        r=n%10
        product=product*r
        n=n//10
    print("Prduct of digits is",product)'''
    
#DESCRIPTION Write a program to read print the sum of the series
'''def f(x):
    return x**(x+1)
sum=0
for i in range(1,8):
    sum=sum+f(i)
print("Sum of series",sum)'''

#DESCRIPTION Write a program to read print the sum of the series
'''def f(x):
    return x**(9-x)
sum=0
for i in range(1,9):
    sum=sum+f(i)
print("Sum of series",sum)'''

#DESCRIPTION Writa a program to print hcf of two numbers
'''a=int(input('Enter first number'))
b=int(input('Enter second number'))
while ( a<= 0 or b<= 0):
    print('invalid data, the numbers have to be positive integers')
    a=int(input('Re-Enter first number:'))
    b=int(input('Re-Enter second number:'))
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
print("hcf of",a,"and",b,"is",hcf)'''

#DESCRIPTION Write a program to compute integration using trapezoidal rule
'''def f(x):
    return 2*x+4
a=int(input("Enter lower limit"))
b=int(input("Enter upper limit"))
n=int(input("Enter number of partions"))
h=float((b-a)/n)
sum=0.5*(f(a)+f(b))
for i in range(1,n):
    sum=sum+f(a+i*h)
sum=h*sum
print("Integration is",sum)'''

#DESCRIPTION Write a program to compute a root of the polynomial using bisection method
'''import math
def f(x):
    return x**3-18*x**2+24
i=-26
t1=50 # to enter into the while loop
# Searching the unit interval
while (t1 > 0 and i<=25):
    i=i+1
    t1=f(i)*f(i+1)
    print(i,i+1,f(i),f(i+1),t1)
if (t1 > 0):
    print('No real root between -25 and 25')
else:
    print('root lies between',i,'and',i+1)
# Apply Bisection
a=i
b=i+1
print(f(a),f(b))
mid=(a+b)/2
k=1
m=math.fabs(f(mid))
while (m > 0.00000000001 and k <=25):
    if (f(a)*f(mid) < 0):
        b=mid
        mid=(a+b)/2
    else:
        a=mid
        mid=(a+b)/2
    m=math.fabs(f(mid))
    k=k+1           
print('root=',mid,'f(root=)',m)'''