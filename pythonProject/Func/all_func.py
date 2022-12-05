#named function
def polynomial(x):
    return x**2 + 5*x + 4
print(polynomial(-4))

#lambda лямбда
print((lambda x: x**2 + 5*x + 4) (-4))
# лямда в переменной
double = lambda x: x * 2
print(double(7))


# map
def add_five(x):
  return x + 5
#
nums = [11, 22, 33, 44, 55]
result = list(map(add_five, nums))
print(result)

# map + lambda
nums = [11, 22, 33, 44, 55]
result = list(map(lambda x: x+5, nums))
print(result)


strip() # удаляет символ

'''Функция rename()
Функция rename() используется для переименовывания файлов в Python. Для ее использования сперва нужно импортировать модуль os.

Синтаксис следующий.
'''
import os
# os.rename(src,dest)

'''
src = файл, который нужно переименовать
dest = новое имя файла
Пример
'''
import os
# переименование xyz.txt в abc.txt
os.rename("xyz.txt","abc.txt")

data = student_data.rstrip('\n').split(':') # rstrip() удаляет указанный символ справа
# пустой strip удаляет последний символ,

'''На примере тестового проекта рассмотрим программу, которая анализирует некоторый файл и определяет какой процент текста приходится на каждый символ.

В этом разделе показано, как файл может быть открыт и прочитан.'''

filename = input("Enter a filename: ")

with open(filename) as f:
   text = f.read()

print(text)

'''Функции all и any, часто используемым в условных инструкциях, можно присваивать список в качестве аргумента; значение True возвращается, когда любой их аргумент (или соответственно все аргументы) возвращает True, в противном случае False. 

Функция enumerate может быть использована для одновременного перебора значений и показателей списка.'''

nums = [55, 44, 33, 22, 11]

if all([i > 5 for i in nums]):
    print("All larger than 5")

if any([i % 2 == 0 for i in nums]):
    print("At least one is even")

for v in enumerate(nums):
    print(v)

'''Чтобы найти наименьшее или наибольшее число или элемент списка, используйте функции max или min.

Чтобы определить расстояние числа от нуля (его абсолютную величину), используйте функцию abs.

Чтобы округлить число до определенного количества знаков после запятой, используйте функцию round.

Чтобы сложить числа в списке, используйте функцию sum.'''

print(min(1, 2, 3, 4, 0, 2, 1))
print(max([1, 4, 9, 2, 5, 6, 8]))
print(abs(-99))
print(abs(42))
print(sum([1, 2, 3, 4, 5]))

'''В Python есть много полезных встроенных функций и методов выполнения частых задач. 

join - объединение последовательности строк с использованием другой строки в качестве разделителя. 

replace - замена одной подстроки на другую.

startswith и endswith - определяют, есть ли подстрока соответственно в начале или в конце строки. 

Для изменения регистра строки используются методы lower (нижний) и upper (верхний).

Метод split - противоположный join, делает из строки с определенным разделителем список. '''

print(", ".join(["spam", "eggs", "ham"]))
#prints "spam, eggs, ham"

print("Hello ME".replace("ME", "world"))
#prints "Hello world"

print("This is a sentence.".startswith("This"))
# prints "True"

print("This is a sentence.".endswith("sentence."))
# prints "True"

print("This is a sentence.".upper())
# prints "THIS IS A SENTENCE."

print("AN ALL CAPS SENTENCE".lower())
#prints "an all caps sentence"

print("spam, eggs, ham".split(", "))
#prints "['spam', 'eggs', 'ham']"

abs()

delattr()

hash()

memoryview()

set()

all()

dict()

help()

min()

setattr()

any()

dir()

hex()

next()

slice()

ascii()

divmod()

id()

object()

sorted()

bin()

enumerate()

input()

oct()

staticmethod()

bool()

eval()

int()

open()

str()

breakpoint()

exec()

isinstance()

ord()

sum()

bytearray()

filter()

issubclass()

pow()

super()

bytes()

float()

iter()

print()

tuple()

callable()

format()

len()

property()

type()

chr()

frozenset()

list()

range()

vars()

classmethod()

getattr()

locals()

repr()

zip()

compile()

globals()

map()

reversed()

__import__()

complex()

hasattr()

max()

round()