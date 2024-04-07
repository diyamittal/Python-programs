def hcf(m1,m2):
    if m1%m2==0:
        return m2
    else:
        return hcf(m2,m1%m2)
n1=int(input("Enter first number"))
n2=int(input("Enter second number"))
if(n1<=0 or n2<=0):
    print("Invalid numbers")
    n1=int(input("Re-Enter first number"))
    n2=int(input("Re-Enter second number"))
if(n1<n2):
    temp=n1
    n1=n2
    n2=temp
u=hcf(n1,n2)
print(u)