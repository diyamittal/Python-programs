#NAME=DIYA ROLL NO:21001003039

# Palindrome without blanks
a="race car" # source string to be checked
#a="never odd or even"
b="" # source string to be created without blanks
for i in range(len(a)):
   if a[i]!=" ": 
       b=b+a[i]
print(b)
k=len(b)
flag=True
for i in range(k):
    if b[i]!=b[k-1-i]:
        flag=False
print("Palindrome status:",flag)