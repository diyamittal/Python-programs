import math
a=int(input("Enter first coefficient"))
b=int(input("Enter second coefficient"))
c=int(input("Enter third coefficient"))
if(a==0):
    print("Invalid input")
d=b*b-4*a*c
if(d>=0):
        r1=(-b+math.sqrt(d))/(2*a)
        r2=(-b-math.sqrt(d))/(2*a)
        print("Roots are",r1,r2)
else:
    d=-d
    real=-b/(2*a)
    img=math.sqrt(d)/(2*a)
    print("root 1 =",real,"+","i",img)
    print("root2 = ",real,"-","i",img)