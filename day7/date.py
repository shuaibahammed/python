import datetime

now=datetime.datetime.now()

print(now.strftime("%d:%m:%Y"))

print(datetime.date.today().month)

x=datetime.datetime(2020,10,7)
y=datetime.datetime(2020,10,2)

dif=x-y
print(dif)