numbers = [1, 2, 3, 4, 5]
print(numbers)
for i in numbers: # для переменной i определяет список и выводит
    print(i)
    print(i*i) # возведение в квадраты

numbers_1 = range(1,6) # range строит списки ДО последнего символа (кроме последнего)
new_list = []
print(numbers_1)
for o in numbers_1:   # перечисление листа с помощью цикла for
    new_list.append(o)
print(new_list)

for t in range (1, 16):
    if t % 2 == 0:
        print(f'{t} четное число') # если t (число) делится на 2 без остатка (0) то выводит строку...
    else:
        print(f'{t} нечетное число') # в остальных случаях....

numbers = [1, 2, 3, 4, 5]
for p, item in enumerate(numbers): # добавляет 10 к числам. enumerate перезаписывает индекс
     numbers[p] += 10
print(numbers)

name = 'обама чмо'
for w in name:
    print(w)

for _ in range (1,3):
    print('касяк!')

some_tuple = (11, 'Alex', 3.14)
for x in some_tuple:
    print(x)

some_list = [('John', 22), ('Alex', 33), ('Artem', 44)]
for (name, age) in some_list:
    print(f'{name} is {age} years old')

some_dict = {
    'Alex': 111,
    'Maxim': 222,
    'Anna': 333}

for m in some_dict:
    print(m)
for n in some_dict.items():
    print(n)
print(type(n))

for b, v in some_dict.items():
    print(f'Ключ {b} и Значение {v}')

for value_1 in some_dict.values():
    print(value_1)