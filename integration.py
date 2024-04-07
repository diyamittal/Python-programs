def f(x):
    return x
a=int(input("Enter lower limit"))
b=int(input("Enter upper limit"))
n=int(input("Enter number of partitions"))
h=float((b-a)/n)
sum=0.5*(f(a)+f(b))
for i in range(1,n):
    sum=sum+f(a+i*h)
sum=h*sum
print("Integration is",sum)
