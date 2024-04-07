n=int(input('Enter the required number of terms: '))
while(n<=3):
    print('Number of terms should be 3 or more')
    n=int(input('Enter the required number of terms: '))    
i=0
j=1
print(i,end=' ')
print(j,end=' ')
count=2
while (count <=n):
    count+=1
    k=i+j
    print(k,end=' ')
    i=j
    j=k