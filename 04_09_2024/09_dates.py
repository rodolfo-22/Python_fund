#fechas

from datetime import datetime

now = datetime.now()

print(now.year)
print(now.month)
print(now.day)
print(now.hour)
print(now.minute)
print(now.second)

year_2023 = datetime(2023, 1, 1)    
print(year_2023)

from datetime import time
print("segunda parte (time)")

current_time = time()
print(current_time.hour)

from datetime import date

today = date(2022,10,6)
print(today.year)
print(today.month)

from datetime import timedelta

time_delta = timedelta()
#se trata para trabajar con franjas de fechas
start_timedelta = timedelta(200,days=5)
end_timedelta = timedelta(200, days=10)
print(end_timedelta - start_timedelta)
print(start_timedelta + end_timedelta)



