#NAME=DIYA ROLL NO:21001003039

#recursive function for fibonacci sequence
def fib(n):     #sum of digits function   
    if (n==0):  
        return 0
    else:
        if (n==1):
            return 1
        else:
            return fib(n-2)+fib(n-1)  
k=int(input('Enter the required number of terms: '))  
t=fib(k)   
print(k,'th fibonacci term is:',t)
