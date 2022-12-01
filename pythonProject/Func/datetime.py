#################   Вычисление разницы между датами
from datetime import date

# Задает первую дату
time_one = date(2020, 10, 1)
# Задает вторую дату
time_two = date(2020, 10, 2)

# Вычисляет расстояние в формате timedelta
delta = time_two - time_one

print(delta)

# Выведет 1 day, 0:00:00

#Создаем время
#При создании времени мы указываем часы, минуты и секунды:

time(<часы>, <минуты>, <секунды>)

from datetime import time

time_one = time(16, 20, 00) # 16 часов 20 минут

print(time_one)

# Выведет 16:20:00

'''Создаем время с датой
При создании времени вместе с датой мы указываем всё вместе, начиная с года и заканчивая секундами, а то, что мы не укажем, считается равным нулю:'''

datetime( <год>, <месяц>, <число>, <часы>, <минуты>, <секунды>)

from datetime import datetime

datetime_one = datetime(1986, 4, 26, 1, 23, 47) # 26 апреля 1986 01:23:47

print(datetime_one)

# Выведет 1986-04-26 01:23:47

# Также есть функция weekday(), которая вернет день недели:
from datetime import date

thedate = date(1970, 1, 5)

print(thedate.weekday())

# Выведет  0, ведь понедельник — нулевой день недели!


# текущая дата и время

from datetime import datetime

thedate = datetime.now()

print(thedate)

'''Форматирование даты
Если вам не нравится доставать время и дату по кусочкам, можно форматировать ее с помощью метода '''
strftime()
 '''(от string format time) и специальной строки-шаблона, например:'''

from datetime import date

thedate = date(1970, 1, 5)

date_formatted = thedate.strftime("%d %B %Y ") # День Месяц Год

print(date_formatted)

# Выведет 05 January 1970
# Вот какие буквы вы можете использовать:

'''%y
Год, короткая версия
18
%Y
Год, полная версия
2018
%m
Месяц номером
04
%B
Месяц словом
April
%d
День, от 01 до 31
12
%H
Час, от 00 до 23
04
%M
Минуты, от 00 до 59
23
%S
Секунды, от 00 до 59
07'''

from datetime import date    

date_1 = date(2017, 10, 20)
date_2 = date(2021, 1, 31)
date_3 = date(2015, 8, 5)

# Не удаляйте код дальше, он нужен для проверки

format = "%d %B %Y"

print(date_1.strftime(format))
print(date_2.strftime(format))
print(date_3.strftime(format))