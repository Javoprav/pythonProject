students = {
    'alex' : 258, 'max' : 227,
    'anna' : 278,
    'жора' : 111
}
print(students)
print(students['anna']) # выводит значение ключа из словаря
print(students.get('alex')) # выводит значение ключа
print(students['жора'])
students['andrey'] = 268 # добавление ключа и значения в словарь
print(students)
students['andrey'] = -3 # изменение так же с помощью добавления
students.setdefault('oleg') # добавляет ключь с пустым значением
print(students)
students.pop('oleg') # pop вырезает ключь
print(students)
print(students.keys()) # выводит ключи без значений
print(type(students.keys())) # тип словаря ключей
key_list = list(students.keys()) # определяет переменной значение списка ключей
print(key_list)
print(type(key_list))
print(students.values()) # выводит значения ключей
print(type(students.values()))
key_vallues = list(students.values()) # определение переменной значений листа
print(key_vallues)
print('anna' in students) # in показывает есть ли определенный ключь в словаре
print('peter' in students)
print('peter' not in students) # not in НЕТ ли определенного ключа в словаре
