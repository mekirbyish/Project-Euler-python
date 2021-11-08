#01/01/1900 is monday
current_day=1
sundays=0
#30:April, June, September, November
#month30=[4, 6, 9, 11]
#31:January, March, May, July, August, October, December
#month31=[1, 3, 5, 7, 8, 10, 12]
#28:February
#february=28
#29:February on leap years
#februrary=29
#leap year: years divisible by 4, except centuries unless divisible by 400
#february=29
#How many sundays on #/01/1901-2000

months=[31,28,31,30,31,30,31,31,30,31,30,31]

date=[1,1,1900]
while date[2]<2001:
    #Februrary shenanigans
    if date[2]%4==0:
        if date[2]%100==0:
            if date[2]%400==0:
                months[1]=29
            else:
                months[1]=28
        else:
            months[1]=29
    else:
        months[1]=28
    #test if first of a month is a sunday
    for x in months:
        if x==31:
            current_day+=3
        elif x==30:
            current_day+=2
        elif x==29:
            current_day+=1
        elif x==28:
            current_day+=0
        current_day%=7
        #only care about sundays and year 1901-2000
        if current_day==0 and date[2]>1900:
            sundays+=1
    date[2]+=1
print(sundays)

#day_of_week=[0,1,2,3,4,5,6]
#Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday
#for 31 day month
#+3
#for 30 day month
#+2
#for 28 day month
#+0
#for 29 day month
#+1
#current_day%7 gets a day_of_week number
#looking for 0