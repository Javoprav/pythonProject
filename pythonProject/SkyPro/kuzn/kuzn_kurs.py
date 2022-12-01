'''# Кузница по курсовой 1
Задания по урокам 3-5
### Списки
**Задание 1 - подсчет количества**
Напишите функцию, которая получала бы список булек и возвращала бы количество True в полученном списке.
def count_for_true(elements):
    pass
print(count_for_true([True, True, True]))  # вернет 3
print(count_for_true([False, True, False]))  # вернет 1'''

def count_for_true(elements):
    tr = 0
    for i in elements:
        if i == True:
            tr += 1

    return tr

print(count_for_true([True, True, True]))

'''**Задание 2 - расчет процента**
Напишите функцию, которая получала бы список элементов чисел и возвращала бы долю единиц в списке
def count_for_ones(elements):
    pass
print(count_for_ones([1, 1, 0, 0]))  # вернет 0.5
print(count_for_ones([0, 0, 0, 0]))  # вернет 0.0
print(count_for_ones([1, 1, 1, 1]))  # вернет 1'''

def count_for_ones(elements):
    edn = 0  # или вместо цикла edn = elements.count(1)
    for i in elements:
        if i == 1:
            edn += 1
    proc = edn / len(elements)
    return proc

print(count_for_ones([1, 1, 0, 0]))
print(count_for_ones([0, 0, 0, 0]))
print(count_for_ones([1, 1, 1, 1]))

'''**Задание 3 - проверка строк**
Напишите функцию, которая проверяет, все ли элементы в списке начинаются с “а”
def check_if_a_is_first(strings):
		pass
print(check_if_a_is_first(["a"]))  # вернет True
print(check_if_a_is_first(["a", "Aaa", "aloha"]))  # вернет True
print(check_if_a_is_first(["a", "boo", "aloha"]))  # вернет False
print(check_if_a_is_first(["b", "c", "d"]))  # вернет False'''

def check_if_a_is_first(strings):
    tr_fo = True
    for i in strings:
        if i[0] == 'a' or i[0] == 'A':
            tr_fo = True
        else:
            tr_fo = False
            break

    return tr_fo

print(check_if_a_is_first(["a"]))  # вернет True
print(check_if_a_is_first(["a", "Aaa", "aloha"]))  # вернет True
print(check_if_a_is_first(["a", "boo", "aloha"]))  # вернет False
print(check_if_a_is_first(["b", "c", "d"]))  # вернет False'''

'''**Задание 4**
Напишите функцию, которая получит список строк, а вернет список их первых букв:
def get_first_letters(strings):
print(get_first_letters(["Alpha", "Bravo", "Charlie"])) # >>  ["A","B","C"]'''

def get_first_letters(strings):
    list_1 = []
    for i in strings:
        list_1.append(i[0])
    return list_1

print(get_first_letters(["Alpha", "Bravo", "Charlie"]))

'''**Задание 5 - случайные числа**
Напишите функцию, которая получит два случайных числа 1-100 и вернет их в виде списка'''

import random

def get_two_randoms():
    list = []
    num = random.randint(1, 100)
    num2 = random.randint(1, 100)
    list.append(num)
    list.append(num2)
    return list
print(get_two_randoms())

'''**Задание 6 - создание словаря**
Напишите функцию, которая получит список и вернет словарь с указанием минимального и максимального числа. Испольуйте функции max, min, len'''
def get_info_from_list(numbers):
    max = 0
    min = 1111110
    for i in numbers:
        if i > max:
            max = i
        if i < min:
            min = i
    
    return {"min": min , "maх": max , "len": numbers}
print(get_info_from_list([1, 5, 10, 15])) 
# вернет {"min": 1, "max": 10, "len": 4}

'''**Задание 7 - перебор списка**
Напишите функцию, которая получит список покупок в виде словаря и вернет сумму.'''


def get_sum(purchases):
    sum = 0
    for i in purchases:
        sum += purchases[i]
    return sum
    
my_purchases = {
  "cookies": 400, 
  "milk": 200, 
  "banana": 100, 
  "chocolate": 100
}
print(get_sum(my_purchases)) # вернет 800


'''**Задание 8 – анализ списка**
Напишите функцию, которая получит список покупок в виде словаря и вернет словарь, который будет содержать ключи:
`min` – минимальная покупка
`max` – максимальная покупка
`sum` – cумма покупок'''

def purchase_stats(purchases):
    sum = 0
    min = 500000
    max = 0
    for i,v in purchases.items():
        if v > max:
            max += v
        if v < min:
            min = v
        sum += v
        
    return {"min": min, "max": max, "sum": sum}
    
# для тестирования

my_purchases = {
  "cookies": 400, 
  "milk": 200, 
  "banana": 100, 
  "chocolate": 50
}

print(purchase_stats(my_purchases)) 

# вернет {"min": 50, "max": 400, "sum": 750}


'''**Задание 9 – кодирование**
Напишите функцию, которая закодирует число буквой'''

nums_to_letter = {
"1": "A", 
"2": "B", 
"3": "C", 
"4": "D", 
"5": "E", 
"6": "F", 
"7": "G", 
"8": "H", 
"9": "I", 
"0": "J", 
}

def code_nums_to_letters(number):
    numb = str(number)
    let = ''
    for n in numb:
        let += nums_to_letter[n]
    return let

print(code_nums_to_letters(15)) #>>> "AE"
print(code_nums_to_letters(101)) #>>> "AJA"



'''**Задание 10** – раскодировать обратно
В функцию передается закодированное в прошлом задании строкой число. Превратите его обратно в число, используя словарь letters_to_nums. Обратите внимание, результат должен быть в виде `int`!'''

letters_to_nums = {
  "A": "1" , 
  "B": "2" , 
  "C": "3" , 
  "D": "4" , 
  "E": "5" , 
  "F": "6" , 
  "G": "7" , 
  "H": "8" , 
  "I": "9" , 
  "J": "0" , 
}

def decode(encoded_number):
    int_decod = ''
    for n in encoded_number:
        int_decod += letters_to_nums[n]
    return int_decod

print(decode("CDE")) # вернет 345
print(decode("IJJJ")) # вернет 9000


'''**Задание 11 – фильтр по упоминаниям**
У вас есть список слов в которых есть упоминания типа @cat. 
Положите в список только эти слова, но без символа @'''

def get_mentions(words):
    words_cleear = ''
    words_cleear_l = []
    words_c = ''
    for word in words:
        if word[0] == '@':
            words_cleear += word[1:] + ' '
            words_cleear_l.append(word[1:])
        elif word[0] != '@':
            words_c += word + ' '
            
    return words_cleear, words_cleear_l, words_c
  
words = ["@кот", "@хлеб", "не", "ешь", "@подумай", "теперь", "ешь"]

print(get_mentions(words)) # вернет ["кот", "хлеб", "подумай"]


'''**Задание 12 – статистика строки**
Напишите функцию, которая получит строку и вернет статистику в виде словаря с ключами: 
`wordcount` – количество слов
`symbolcount` – количество символов
`spacecount` – количество пробелов'''


def get_string_stats(string):
    wordcount = 0
    symbolcount = 0
    spacecount = 0
    for s in string:
        if s == ' ':
            spacecount += 1
            wordcount += 1
        #elif s != ' ':
        symbolcount += 1
    return {"wordcount": wordcount+1, "symbolcount": symbolcount, "spacecount": spacecount}

print(get_string_stats("Кот это не хлеб")) 

# Вернет {"wordcount": 4, "symbolcount": 15, "spacecount": 3}


'''**Задание 13**
В списке содержится список чисел строго по возрастанию.
Соберите в отдельный список те, которые НЕ содержатся в исходном списке.'''

def get_missed_between(numbers):
    list_num = []
    for i in range(numbers[0], max(numbers)):
        if i not in numbers:
            list_num.append(i)
    return list_num
    
numbers = [100, 102, 104, 106, 107, 108, 110]

print(get_missed_between(numbers)) # вернет [101, 103, 105, 109]