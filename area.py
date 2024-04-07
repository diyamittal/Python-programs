print("1.Area of square")
print("2.Area of triangle")
print("3.Area of rectangle")
print("4.Area of circle")
o=int(input("Enter your choice"))
if(o==1):
    side=float(input("Enter side of square"))
    area=side*side
elif(o==2):
    h=float(input("Enter height of triangle"))
    b=float(input("Enter base of triangle"))
    area=0.5*b*h
elif(o==3):
    l=float(input("Enter length of rectangle"))
    br=float(input("Enter breadth of rectangle"))
    area=l*br
else:
    r=float(input("Enter radius of circle"))
    area=3.14*r*r
print("Area is",area)
