# Выведите, сколько чисел в строке и сколько букв
# Всего чисел: 6
# Всего букв: 5

line_letters = 0
line_num = 0
line = "13fet35kk54"

for i in line:
    if i.isalpha():
        line_letters += 1
    elif i.isdigit():
        line_num += 1

print(f'Всего чисел: {line_num}\nВсего букв: {line_letters}')

'''### Задание 2

У вас есть строка, посчитайте, какой процент от нее составляют пробелы

```python
line = "13f et3 5kk54"
```

Пример вывода: Пробелов: 2, это 20%'''

line = "13f et3 5kk54"

line_list = line.split()
space = 0

for i in line_list:
    space += 1
print(line_list)
print(f'Пробелов: {space-1}  это {len(line) * (space-1)}%')

#for i in line:
    #if i == " ":                _____решение 2________
        #space += 1

### Задание 3
# У вас есть строка, посчитайте, какое количество слов являются хештегами (начинаются с # решетки)
# сегодня #прогулка# #еда #ко#ты
# ```Всего хешегов: 3

s = '#прогулка# #еда #ко#ты'

ss = s.split()
has = 0

for i in ss:
    if i[0] == '#':
        has += 1

print(f'Всего хешегов: {has}')

### Задание 4
#У вас есть строка, посчитайте количество заглавных букв в ней
#line = "A13f et3 D 5kk54 M"
#```Заглавных букв: 3

line = "A13f et3 D 5kk54 M"
capital = 0

for i in line:
    if i.isupper():
        capital += 1
print(f'Заглавных букв: {capital}')

#### Задание 5
#У вас есть список строк, составьте словарь, где будет длина каждой:
#lines = ["abcd", "ab", "bcdef"]
#``` {1: 4, 2: 2, 3:5}

lines = ["abcd", "ab", "bcdef"]
lines_dict = {}

for i in range(len(lines)):
    lines_dict[i] = len(lines[i]) #__с названиями: lines_dict[lines[i]] = len(lines[i])
print(lines_dict)

### Задание 6
# У вас есть строка. 
# abcdefghijklmnopqrstuvwxyz
# Со стандартного ввода подаются два числа x и y, разделенные дефисом.
# 1-4
# Верните буквы в соответствующем интервале (от x до y) ВКЛЮЧИТЕЛЬНО. Пример вывода
#     bcde

s = 'abcdefghijklmnopqrstuvwxyz'
ss = ""
x = int(input('X: '))
y = int(input('Y: '))

for i in range(x,(y+1)):
    ss += s[i]
print(ss)

## Создание строк
### Задание 1
# Создайте строку numbers, содержащую цифры от 0 до 19
# Создайте строку `letters`, содержащую буквы от a до z
# numbers = ...
# letters = ...
# Не удаляйте эти данные, они нужны для проверки
# print(numbers, letters)

numbers = [str(i) for i in range(0,20)]

numberss = [', '.join(numbers)]

number = ''

for i in numberss:
    number += i
print(numberss)
print(number)

num = ''

for n in range(0,20):
    num += str(n)
    
print(num)

import string
string.ascii_lowercase[:14]
letters = string.ascii_lowercase[:30]
print(letters)

## Работа с индексами
### Задание  2 - Акронимы (работа с индексами)
'''Со стандартного ввода подается название корпорации трех слов, составьте строку из первых букв
Пример ввода
```python
Best
Update
Technologies
```
Пример вывода
```python
BUT
```Сustom
Automatic
Transport

Original
Worldwide
Limited'''

word_1 = input()
word_2 = input()
word_3 = input()

print(word_1[0]+word_2[0]+word_3[0])

### Задание 3 (работа с индексами)
'''У вас есть строка. Со стандартного ввода подается индекс. 
Получите символы на соответствующем месте и выведите его.
```python
# Исходный код
word = "ABCDEFGHIJK"

index = int(input())
```
Пример ввода:

```python
3
```
Пример вывода: D'''

word = "ABCDEFGHIJK"

index = int(input())

print(word[index])

### Задание 2 (перебор строк)
'''У вас есть строка, выведите с помощью цикла все символы, кроме пробелов. Чтобы вывести символы на одной строке используйте print(..., end=””) .
```python
# исходный код
word = "STRINGS ARE AWESOME"
Пример вывода:
STRINGSAREAWESOME'''

word = "STRINGS ARE AWESOME"
word_new = ''

for i in word:
    if i != ' ':
        word_new += i
print(word_new, end=' ')
print(word_new)

