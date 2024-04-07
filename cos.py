import math
a=float(input("Enter angle in degrees"))
x=3.1459*a/180.0
sum=1
alt=-1
fact=1
for i in range(1,9):
    fact=(2*i-1)*(2*i)*fact
    sum=sum+alt*(x**(2*i))/fact
    alt=-alt
print("cos(",a,")=",sum)
s=math.cos(x)
print(s)
    