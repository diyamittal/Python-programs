f=1
k=1
compute=1
n=int(input("Enter number"))
while(n<0 and k<=5):
    print("invalid number")
    n=int(input("Re enter the number"))
    k=k+1
if(k>5):
    compute=0
if(compute==1):
    for i in range(1,n+1):
        f=f*i
    print("factorial of number is",f)
else:
    print("You exceeded the limit")
    