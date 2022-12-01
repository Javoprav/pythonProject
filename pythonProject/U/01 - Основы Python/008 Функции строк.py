x = 'some long and awesome text'
print(len(x)) # сколько символов
print(x[len(x)-1]) # выдаёт определенный символ
print(x[len(x)-4:len(x)])
print(x.count('o')) # count выдает сколько в строке есть определенных символов
print(x.find('a')) # поиск позиции
print(x.find('o', 3, 7))
print(x.find('o', 7))
print(x.find('and'))
print(x.find('abc'))
print(x.capitalize()) # переводит первую букву в верхний регистр
print(x.upper()) # переводит все буквы в верхний регистр
print('Old text: '+x) # показывает старый текст
upper_cased = x.upper() # присвоение переменной функции
lower_cased = x.lower()
print(upper_cased.isupper()) # проверяет находятся ли все символы в верхнем регистре
print(upper_cased.islower())
print(lower_cased.islower())
print(x.isupper())
print('xxx777'.isalnum()) # проверяет состоит ли строка только из букв и чисел
print('xxx777!'.isalnum()) # символ в строке
print('xxx777'.isalpha()) # проверяет состоит ли строка только из букв
print('xxx'.isalpha())
x = str('hello')
print(x.startswith('he')) # проверяет начинается ли строка на he
print(x.endswith('lo'))
split = x.split('l') # вырезает символ
print(type(split))
print(split)
split = x.split('e')
print(split)
some_data = '4;8;15;16;23;42'
separated_data = some_data.split(';')
print(separated_data)
print(separated_data[3])
print(type(some_data))