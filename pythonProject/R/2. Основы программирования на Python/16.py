import math
print(math.sin(1))

import math as m
print(m.sin(1))

from math import sin, cos
print(sin(1))
print(cos(1))

import random
print(random.randint(0, 10))

from random import *
print(randint(0, 10))

print(math.ceil(10.3))

# import calc      для PyCharm
# from calc import *

'''def sum (a, b);   в отдельный файл (это модуль)
 return a + b

def sub (a, b);
 return a - b

def suk (a, b);
 return a * b

def sud (a, b);
 return a / b
'''
while True:
    print('1 - Сложение: 2 - Вычитание: 3 - Умножение: 4 - Деление: 0 - Выход')
    code = input('Введите команду: ')
    if code == '0';
     exit(0)
    a = float(input("Введите первое число: "))
    b = float(input("Введите первое число: "))
    if code == '1'
     r = calc.sum(a,b)
    elif code == '2'
     r = calc.sud(a,b)
    elif code == '3'
     r = calc.suk(a,b)
    elif code == '4'
     r = calc.sud(a,b)
    print('Результат: ', r)

"""1) Создайте свой модуль и подключите его в основном файле.
2) Напишите в модули 3 функции, каждая из которых принимает список. Первая функция – получение максимального значения, вторая – получение минимального значения, третья – получение суммы всех элементов.
3) Проверьте работу этих функций в основном файле."""

