# Задание №1: Реализовать вывод информации о промежутке времени в зависимости от его продолжительности duration в секундах
# 1 вариант решения
import datetime
from datetime import time

duration1 = int(input('введите промежуток времени в часах: '))
duration2 = int(input('введите промежуток времени в минутах: '))
duration3 = int(input('введите промежуток времени в секундах: '))
duration0 = datetime.time(duration1, duration2, duration3)
print(duration0)

# 2-ой вариант решения
duration = int(input('Укажите продолжительность времени в секундах: '))
second = 60
minute = 3600
hour = 86400
day = 2073600

if duration < second:
    print('{} сек'.format(duration))
elif second <= duration and duration < minute:
    minute1 = duration // second
    second1 = duration % second
    print('{} мин {} сек'.format(minute1, second1))
elif minute <= duration and duration < hour:
    hour1 = duration // minute
    duration = duration % minute
    minute1 = duration // second
    second1 = duration % second
    print('{} час {} мин {} сек'.format(hour1, minute1, second1))
elif hour <= duration and duration < day:
    day1 = duration // hour
    duration = duration % hour
    hour1 = duration // minute
    duration = duration % minute
    minute1 = duration // second
    second1 = duration % second
    print('{} д {} ч {} м {} с'.format(day1, hour1, minute1, second1))
