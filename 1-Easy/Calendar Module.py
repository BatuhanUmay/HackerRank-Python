# >>> import calendar
# >>> 
# >>> print calendar.TextCalendar(firstweekday=6).formatyear(2015)

import calendar

# print(calendar.TextCalendar(firstweekday = 5).formatyear(2021))


ay,gun,yil = map(int, input().split())

print((calendar.day_name[calendar.weekday(yil,ay,gun)]).upper())






