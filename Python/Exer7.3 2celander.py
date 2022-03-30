from datetime import timedelta
import datetime
x=datetime.datetime(2022,1,1)
y = timedelta(days=31)

for i in range(1,13):
    x+=y
    print("month",i,",","date",x)