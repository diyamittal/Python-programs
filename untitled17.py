#NAME=DIYA ROLL NO:21001003039

# day corresponding to a date
import math
def leap(year):
    if ((year%400==0)or(year%100!=0 and year%4==0)):
        return 1
    else:
        return 0
dd=int(input('Enter date:'))
mm=int(input('Enter month:'))
yy=int(input('Enter year:'))
c_year=yy-1 # number of completed years
c_month=mm-1 # number of completed months

excess_days=math.floor(c_year/100)*5+math.floor(c_year/400) # excess days corresponding to completed centuries
print(excess_days)

excess_days=excess_days + c_year % 100+math.floor(c_year%100/4) # excess days corresponding to years
# excess days corresponding to completed months

e_day=[0,31,59,90,120,151,181,212,243,273,304,334] #excess days corresponding to month
print(e_day[c_month])
excess_days=excess_days+e_day[c_month]+dd
if (mm > 2):
    excess_days=excess_days+leap(yy)
k=excess_days % 7
day=["sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"]
print(day[k])
