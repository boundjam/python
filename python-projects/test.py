import datetime
today = datetime.date.today()
days_until_zachs_bday = datetime.date(2019,9,25 )
days_until_daddys_bday = datetime.date(2019,7,20)
days_until_mommys_bday = datetime.date(2019,12,8)
days_until_emmas_bday = datetime.date(2019,7,9)
zach = 'There are '+ str(days_until_zachs_bday - today)
daddy = 'There are '+str(days_until_daddys_bday -  today)
mommy = 'There are '+str(days_until_mommys_bday -  today)
emma = 'There are '+str(days_until_emmas_bday -  today)
zach = zach[0:-9]
señur_days = int(zach[9:-5])
daddy = zach[0:-9]
BIG_señur_days = int(zach[9:-5])
print(señur_days)