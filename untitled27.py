#NAME=DIYA ROLL NO:21001003039

# square root of a number
n=float(input('Enter the number: '))
s=n  #5
y=1  
e = 0.0000001 # error allowed/ tolerance
while (s - y) > e:          
    s = (s + y) / 2 # s=3,2.355,2.2355 
    y = n / s     #1.71,2.12,2.38  
    print(s,y)  # see convergence
print(s)

