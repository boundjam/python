import datetime


def find_time(munth,doy,name):
    d = datetime.datetime.today()
    this_month = d.month
    this_day = d.day
    number_of_months = str(munth - this_month)
    number_of_days = str(doy - this_day)
    closing_string ='there is '+number_of_months +' months and '+ number_of_days+' days until '+ name +' birthday'
    return number_of_months,number_of_days,closing_string


if __name__ == "__main__":
    zach = find_time(9,25,'zach\'s')
    emma = find_time(7,9,'emma\'s')
    daddy = find_time(7,20,'daddy\'s')
    mommy = find_time(12,8, 'mommy\'s')
    d = str(datetime.date.today().year)
    dates =  ["9/25/"+d, '7/9/'+d, "7/20/"+d,"12/8/"+d]
    dates.sort(key = lambda date: datetime.datetime.strptime(date, '%m/%d/%Y'))
    for i in range(0,4):
        if dates[i] == '7/9/'+d:
            print(emma[-1]) 
        elif dates[i] == "7/20/"+d:
            print(daddy[-1])
        elif dates[i] == "9/25/"+d:
            print(zach[-1])
        else:
            print(mommy[-1])