import math
d=float(input("Enter angle in degrees"))
x=3.1459*d/180.0
sum=x
alt=-1
fact=1
for i in range(1,9):
    fact=(2*i+1)*(2*i)*fact
    sum=sum+alt*(x**(2*i+1))/fact
    alt=-alt
    
print("sin(",d,")=",sum)
s=math.sin(x)
print(s)