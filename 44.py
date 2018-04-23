import time
#this is the the part asking what year you want
print("pick a number 1 - 10 for the first digit of the year")
r1=input()
print('pick a number 1 - 10 for the second digit of the year')
r10=input()
print('pick a number 1 - 10 for the third digit of the year')
r100=input()
print('pick a number 1 - 10 for the fourth digit of the year')
r1000=input()
d=r1000*1000
z=r100*100
x=r10*10
c=d+z+x+r1
#month
print('what is the month you want')
my=input()
#day of month
print('do you want a 2 digit day of the month?')
a=input()
if a == 'no':
    print('pick a number 1 - 10 for the day of the month')
    md=input()
elif a == 'yes':
    print('pick a number 1 - 10 for the 1 digit of the month day')
    md1=input()
    m=md1*10
    print('pick a number 1 - 10 for the 2 digit of the month day ')
    md2=input()
    md=m+md2
#hour
l=input()
if l == 'no':
    print('pick a number 1 - 10 for the hour')
    h=input()
elif l == 'yes':
    print('pick a number 1 - 10 for the 1 digit of the hour ')
    h1=input()
    print('pick a number 1 - 10 for the 2 digit of the hour ')
    h2=input()
    hh=md1*10
    h=hh+h2
#minute
i=input()
if i == 'no':
    print('pick a number 1 - 10 for the minute')
    mi =input()
elif i == 'yes':
    print('pick a number 1 - 10 for the 1 digit of the minute')
    mi1=input()
    print('pick a number 1 - 10 for the 2 digit of the minute')
    mi2=input()
    mii=mi1*10
    mi=mii+mi2
#second
o=input()
if o == 'no':
    print('pick a number 1 - 10 for the second')
    sec=input()
elif o == 'yes':
    print('pick a number 1 - 10 for the 1 digit of the second')
    sec1=input()
    print('pick a number 1 - 10 for the 2 digit of the second')
    sec2=input()
    secc=sec1*10
    sec=secc+sec2
#day of week
print('pick a number 1 - 10 for the day of the week')
w=input()
#daylight saving mode or not
print('do you want daylight saving mode or not')
d0=input()
if d0=='yes':
    da=1
elif d0=='no':
    da=0
t=[c,my,md,mi,sec,w,0,da,]
print(time.asctime(t))
