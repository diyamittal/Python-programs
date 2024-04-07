def big(x,y):
    if(x>y):
        return x
    else:
        return y
a=int(input("Enter first number"))
b=int(input("Enter second number"))
t=big(a,b)
print("Greatest number is",t)