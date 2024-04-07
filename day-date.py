import math
t=1
dd=int(input("Enter date"))
mm=int(input("Enter month"))
yy=int(input("Enter year"))
if(yy%100==0 and yy%400==0 or yy%100!=0 and yy%4==0):
    t=1
else:
    t=0
list1=[0,3,3,6,8,11,13,16,19,21,24,26]
list2=['Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday']
excess_days=0
y=yy-1
m=mm-1
y=y%400
excess_days=math.floor((y/100)*5) + (y%100)+math.floor((y%100))/4 + list1[m]+dd
if(t==1 and mm>=2):
    excess_days+=1
k=int(excess_days%7)
print(list2[k])
#12/10/2004