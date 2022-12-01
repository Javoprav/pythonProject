'''### Задача 1
Напишите функцию `print_square()`, которая печатает квадрат 2 на 4, вот такой
****
****
'''

def print_square():
    str_1 = ''
    str_2 = ""
    x = int(input("Введите число: "))
    for i in range(x):
        str_1 += '*'
        str_2 += '*'
    print(f'{str_1}\n{str_2}')

print_square()


'''### Задача 2
Напишите функцию `print_line(x)` которая печатает строку звездочек выделенной длины
# Если x = 7
*******
'''

def print_line(number):
    print("*" * number)
    #str_1 = ''
    #for i in range(x):
    #    str_1 += '*'
    #print(f'{str_1}')

print_line(5)


'''### Задача 3

Напишите функцию `print_square(x,y)` , которая печатает прямоугольник со сторонами X, Y
# Если x = 4, y=2

****
****

# Если x = 4, y=4

****
****
****
**** '''

def print_line(x,y):
    for i in range(y):
        print('*' * x)


x = int(input())    
y = int(input()) 
print_line(x,y)

'''### Задача 4
Напишите функцию `get_grade(grade)`, которая принимает целое число от 2 до 5 и возвращает оценку
Плохо
Удовлетворительно
Хорошо
Отлично
'''

def get_grade_verbose(grade):
    if grade == "2":
        print("Плохо")              ########   или return без print
    elif grade == '3':
        print("Удовлетворительно")
    elif grade == '4':
        print("Хорошо")
    elif grade == '5':
        print("Отлично")

grade = input('Ввод: ')

get_grade_verbose(grade)

'''### Задача 5
Напишите функцию `get_square(radius)`, которая возвращает площадь кружочка.
Функция принимает радиус кружочка
Площадь кружочка = `радиус ** 2 * Пи`
Пи можно считать равным 3.14 или получить из math.pi (math нужно будет импортировать)'''

def get_square(radius):
    pl = radius ** 2 * 3.14
    return pl


radius = int(input())
print(get_square(radius))

'''### Задача 6
Напишите функцию `get_period(hour)` которая принимает целочисленный час суток 0-24 и возвращает
0-6 ночь
7-11 утро
12-17 день
18-24 - вечер '''

def get_period(hour):
    
    if hour in range(0,7):
      return "ночь"
    if hour in range(7,12):
      return "утро"
    if hour in range(12,18):
      return "день"   
    if hour in range(18,24):
      return "вечер"

hour = int(input())

print(get_period(hour))

'''### Задача 7
Напишите функцию `get_grade(x)`, которая принимает целочисленные баллы (0-100) и возвращает
0-40 Плохо
41-60 Удовлетворительно
61-80 Хорошо
81-100 Отлично '''

def get_grade(points):
  
  if points < 41:
    return "Плохо"
  if points < 61:
    return "Удовлетворительно"    
  if points < 81:
    return "Хорошо"   
  return "Отлично"

print(get_grade(67))

'''### Задача 8
Напишите функцию `avg(items)`, которая принимает список и вычисляет среднее арифметическое элементов в виде целого числа. Например, `avg([1,2,3])` вернет 2
Подсказка: среднее арифметическое'''

def avg(items):
    sum = 0
    for i in items:
        sum += i

    sr_a = sum / len(items)
    return sr_a

print(avg([1,2,3]))

'''### Задача 9
Напишите функцию `has_rrr(word)`, которая проверяет картавость слова, а возвращает булево значение.
Например `has_rrr(”речка”)` вернет True
Например `has_rrr(”уточка”)` вернет False'''

def has_rrr(word):
    if "р" in word or "Р" in word:
        return True
    else:
        return False

print(has_rrr("речка"))
print(has_rrr("Месси"))
print(has_rrr("Роналду"))
print(has_rrr("Чалов"))

"""Напишите функцию the_longest(words), которая возвращает самое длинное слово из списка. Например the_longest(["еж" , "вещь", "стриж"]) вернет "стриж"""

def the_longest(words):
    long_word = ""
    for word in words:
        if len(word) > len(long_word):
            long_word = word
    return long_word

print(the_longest(["еж" , "вещь", "стриж", "леонельмессина"]))

# word = input().split(" ")
# result = the_longest(word)
# print(result)

'''У вас есть `get_rur_kop(value)` сумма в копейках, верните количество полных рублей 
Подсказка: деление нацело x//y , остаток от деления: x%y
Например: `get_rur_kop(230)` вернет 2
Например: `get_rur_kop(590)` вернет 5'''

def get_rur_kop(value):
    rub = value // 100
    return rub

print(get_rur_kop(590))

'''### Задача 12
Напишите функцию `get_min_sec(sec)` которая принимает время в секундах, возвращает словарь в формате `{”min”: мин, “sec”: сек)}`. Минуты и секунды  целые числа.
Пример `get_min_sec(120)` Вернет `{”min”:2, “sec”:0}`
Пример `get_min_sec(150)` Вернет `{”min”:2, “sec”:30}`
Пример `get_min_sec(15)` Вернет `{”min”:, “sec”:15}`
Подсказка: деление нацело x//y , остаток от деления: x%y'''

def get_min_sec(sec):
    dict_time = {}
    min = sec // 60
    sec_ = sec % 60
    dict_time['min'] = min
    dict_time['sec'] = sec_
    return dict_time

print(get_min_sec(120))
print(get_min_sec(150))
print(get_min_sec(15))

# value = int(input())
# result = get_min_sec(value)  
# print(result)

'''### Задача 13
Напишите функцию `get_discount(summ)` которая возвращает уровень скидки или бонусной карты в зависимости от суммы покупок. Уровень – это целое число! Правила вычисления уровня:
1 до 5000
2 до 10000
3 до 20000
4 до 35000
5 до 50000
6 от 50000 и выше
Например `get_discount(7000)` возвращает 2'''

def get_discount(summ):
    if summ < 5000:
      return 1
    elif summ < 10000:
      return 2
    elif summ < 20000:
      return 3
    elif summ < 35000:
      return 4
    elif summ < 50000:
      return 5
    else:
      return 6    
    
# Не удаляйте код ниже, он нужен для проверки

value = int(input())
result = get_discount(value)  
print(result)

'''### Задача 14
Напишите функцию `get_price_with_discount(price, percentage)` которая получает сумму и уровень скидок и возвращает цену с плавающей точкой(`price` - это цена. `percentage` - процент скидки, целое число. )
Например:
`get_price_with_discount(1000, 10)` возвращает 900.0
`get_price_with_discount(500, 50)` возвращает 250.0'''

def get_price_with_discount(price, percentage):
    sum = (percentage * price) / 100
    sum_ = price - sum
    return sum_

price = int(input())
percentage = int(input())
result = get_price_with_discount(price, percentage)  
print(result)

'''### Задача 15
Напишите функцию `get_price_with_discount(price, level)`, которая получает сумму и уровень скидок и возвращает цену с плавающей точкой(`price` - это цена. `level` - уровень скидки, целое число. )
'Уровень 1':10%,
'Уровень 2':25%,
'Уровень 3':50%
Например:
`get_price_with_discount(1000, 1)` возвращает 900.0
`get_price_with_discount(500, 3)` возвращает 250.0'''

def get_price_with_discount(price, level):
    dict_prise = {1:10, 2:25, 3:50}
    sum = (price * dict_prise[level]) / 100
    sum_ = price - sum
    return sum_

price = int(input())
level = int(input())
result = get_price_with_discount(price, level)  
print(result)


'''### Задача 16
У вас есть текст в котором встречаются #хештеги
Напишите функцию `get_hash(text)`
Верните все хештеги одним списком
Например:
`get_hash("Котята #еда #закат море")` вернет [”#еда”, “#закат”] 
`get_hash("Котята море")` вернет [] 
Подсказка: Разбейте текст на слова, затем проверьте не решетка ли первый символ'''

def get_hash(text):
    tex = []
    for t in text.split(" "):
        if t[0] == '#':          ### or ###   if element.startswith("#"):
            tex.append(t)        ### срез без хэш ### hashtags.append(element[1:])
    return tex
            
print(get_hash("Котята #еда #закат море"))

#   words = input()
#   result = get_hashtags(words)
#   print(" ".join(result))


'''### Задача 17
У вас есть текст в котором встречаются хештеги и упоминания .
Напишите функцию `get_hashes_and_mentions(text)`
Функция должна возвращать словарь типа {"hashes": ..., "mentions": ...}
Например:
`get_hashes_and_mentions("Котята #еда @Вася море")` 
вернет 
{"hashes": [”#еда”], "mentions": [”@Вася”]}'''

def get_hashes_and_mentions(text):
    tex = {}
    for t in text.split(" "):
        if t[0] == '#':          ### or ###   if element.startswith("#"):
            tex["hashes"] = t           ### срез без хэш ### hashtags.append(element[1:])
        elif t[0] == '@':
            tex["mentions"] = t
    return tex
            
print(get_hashes_and_mentions("Котята #еда @Вася море"))

#   words = input()
#   result = get_hashtags(words)
#   print(" ".join(result))

