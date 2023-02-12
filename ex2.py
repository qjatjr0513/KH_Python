# from datetime import date
# from datetime import time
# from datetime import datetime
from datetime import datetime, timedelta
# today = date.today()

# print(today)

# new_date = date(1999, 12, 31)
# print(new_date)

# print(time(9))
# print(time(9,2))
# print(time(9, 2, 2))
# print(time(9, 2, 2, 2222))

# dt = datetime.now()

# print(dt)
# dt = datetime(2002, 10, 20, 14, 5, 2)
# print(dt)

# today = datetime.now()
# print(today - timedelta(days = 20))
# print(today + timedelta(days = 20, hors = , weeks=, minutes=))

# import time
# now = time.time()

# print(now)

# from time import localtime

# now = localtime()
# print(now)

from time import strftime

now = strftime("%Y-%m-%d %H:%M")
now2 = strftime("%Y년 %m월 %d일 %H시 %M분")
print(now)
print(now2)

