#NAME=DIYA ROLL NO:21001003039

#program for even odd
n=int(input("Enter any number"))
if(n<0):
    print("Enter positive number")
    n=int(input("Re-enter the number"))
if(n%2==0):
    print("Number is even")
else:
    print("Number is odd")
    