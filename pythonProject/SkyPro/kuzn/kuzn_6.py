'''# PD кузница урок 6
### Задание 1:
Получить из файла data.txt строку и вывести ее в консоли
# data.txt:
Все работает
# Пример вывода:
Все работает'''

with open('data.txt', 'r', encoding='utf-8') as f:
    print(f.read())

    # for line in f.readlines():    # или так #
    # print(line)

'''### Задание 2:
Получить из файла data.txt все строки вывести построчно
# Пример файла:
Содержимое файла
Выводится посточно
И это отлично
# Пример вывода:
Содержимое файла
Выводится посточно
И это отлично'''

with open('data.txt', encoding='utf-8') as f:
    for i in f.readlines():
        print(i)

'''### Задание 3:
Получите из файла записанный построчно список, превратите его в тип list, выведите построчно
# Пример файла:
Alpha
Bravo
Charlie
Delta
Echo'''

line_list = []

with open('data.txt', 'r', encoding='utf-8') as f:
    for i in f:
        line_list.append(i)

for num, line in enumerate(line_list, start=1):
    print(num, line)

print([(a, b) for a, b in enumerate(line_list)])  # тестовый вариант

'''### Задание 4
Получите из файла записанный построчно список расходов, превратите его в тип list, просуммируйте, найдите среднее.
# Пример файла:
1500
750
1350
1100
800
# Пример вывода:
Сумма: 5400
Среднее: 950'''

line_list = []

with open('data.txt', 'r', encoding='utf-8') as f:
    for i in f:
        line_list.append(int(i))

summ = sum(line_list)

sr = summ / len(line_list)

print(f'Сумма: {sum}\nСреднее: {sr}')

'''### Задание 5
Напишите функцию `load_list_from_file(path)` которая получает из файла, путь которого передан,  список и возвращает его в виде типа list.
# Пример файла:
2015
2016
2017
2018
2019
2020
2021
# Пример вывода:
[2015, 2016, ...]'''


def load_list_from_file(path):
    line_list = []
    with open(path, 'r', encoding='utf-8') as f:
        for i in f:
            line_list.append(i.strip())
    return line_list


print(load_list_from_file('data.txt'))

'''### Задание 6
Напишите функцию `load_dict_from_file(path)` которая получает из файла, путь которого передан, список и возвращает его в структуре данных  `dict` - ключи в числах, значения в строках
# Пример файла:
1 A
2 B
3 C
4 D
# Пример вывода:
{1:"A", 2: "B", 3: "C", ...}'''
import os


def load_dict_from_file(path):
    line_list = {}
    with open(path, 'r', encoding='utf-8') as f:
        for i in f.readlines():
            ii = i.replace(" ", "")
            line_list[ii[0]] = ii[1]
    return line_list


my_path = os.path.join('SkyPro', 'Lesson', '6,2', 'data.txt')

print(load_dict_from_file(my_path))

'''### Задание 7
Получите от пользователя строку со стандартного ввода.
Запишите ее в файл recorded.txt'''

user_inp = input()

with open('recorded.txt', 'a', encoding='utf-8') as f:
    f.write(user_inp)

'''### Задание 8
Получите от пользователя три строки со стандартного ввода
Запишите их тремя отдельными строками в файл
friendship
is
magic'''

user_data = []

for i in range(3):
    user_inp = input()
    user_data.append(user_inp)

for line in user_data:
    with open('recorded.txt', 'a', encoding='utf-8') as f:
        f.write(line + '\n')
        # №№№№№№№№№№№№№№№ то  же самое
'''with open('recorded.txt', 'a', encoding='utf-8') as f:
    for line in user_data:
        f.write(line + '\n')'''


####################### или с функциями
def get_user_input():
    user_data = []

    for i in range(3):
        user_inp = input()
        user_data.append(user_inp)
    return user_data


def write_to_file(user_data, path):
    with open(path, 'a', encoding='utf-8') as f:
        for line in user_data:
            f.write(line + '\n')


data = get_user_input()
write_to_file(data, 'recorded.txt')

'''### Задание 10
Получите от пользователя число от 1 до 5 со стандартного ввода.
Создайте соответствующее количество файлов типа 1.txt 2.txt 3.txt и так далее
В каждом файле разместите строку “файл создан”
###'''
#
user_input = input()

for i in range(int(user_input)):
    path = f'{i}.txt'
    with open(path, 'a') as f:
            f.write('файл создан')