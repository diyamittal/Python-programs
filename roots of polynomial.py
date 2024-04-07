def f(x):
    return x**3+5*x**2+7*x-11
flag=0
i=-50
while(flag==0 or i<=50):
    a=f(i)
    b=f(i+1)
    c=a*b
    if(c<=0):
        flag=1
        i=i+1
a=i
b=i-1
c=(a+b)/2
while(abs(f(c))>0.000001):
    if(f(a)*f(c)<0):
        b=c
    else:
        a=c
    c=(a+b)/2
print(c)
