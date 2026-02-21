import datetime

#Present date and time
now = datetime.datetime.now()
print(now)

#Creating a specific date
d = datetime.datetime(2026, 2, 21)
print(d)

#Only year,month,day
today = datetime.date.today()
print(today.year)
print(today.month)
print(today.day)

#Difference between two dates
d1 = datetime.date(2026, 1, 1)
d2 = datetime.date(2026, 2, 21)

difference = d2 - d1
print(difference.days)

#Time formatting (strftime)
now = datetime.datetime.now()
formatted = now.strftime("%d-%m-%Y %H:%M:%S")
print(formatted)