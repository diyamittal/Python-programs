#NAME=DIYA ROLL NO:21001003039

# factorial by recursion
def f(x):
    if (x==0):   
        return 1   # terminal definition
    else:
        return x*f(x-1)  #recursive dfinition
n=int(input('Enter the number:'))
k=f(n)
print(n,'!=',k)