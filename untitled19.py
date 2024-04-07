#NAME=DIYA ROLL NO:21001003039

# checking the string for palindrome
a=input('Enter the string:') #,malayalam
n=len(a) #9
flag=True
for i in range(n//2): # n=4,i=0,1,2,3
    if a[i]!=a[n-1-i]:
        flag=False
if flag:
    print('String is palindrome')
else:
    print('string is not palindrome')
    