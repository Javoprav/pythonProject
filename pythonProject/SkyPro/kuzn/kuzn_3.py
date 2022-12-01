'''**Задача 1**

В списке есть несколько чисел. 

```python
numbers = [4,5,7,8,10]
```

Пользователь  вводит с клавиатуры число. Выведите в зависимости от попадания  числа в предоставленный ряд:

```python
Число есть / Числа нет
```'''

numbers = [4,5,7,8,10]

user_input = int(input()) #
if user_input in numbers: # или int(user_input)
    print('Число есть')
else:
    print('Числа нет')

print

'''**Задача 2**

В списке есть несколько чисел. 

```python
numbers = [4,5,7,8,10]
```

Пользователь  вводит с клавиатуры два числа. Выведите в зависимости от попадания этих чисел в предоставленный ряд

Оба числа есть
Одно из чисел есть
Ни одного из чисел нет'''

numbers = [4,5,7,8,10]

user_input1 = int(input('Введите число 1: '))
user_input2 = int(input('Введите число 2: '))

if user_input1 and user_input2 in numbers:
    print('Оба числа есть')
elif user_input1 in numbers or user_input2 in numbers:
    print('Одно из чисел есть')
else:
    print('Ни одного из чисел нет')

'''**Задача 3**

В списке есть несколько чисел. Просуммируйте только те, которые меньше 10.

```python
numbers = [10, 4, 5, 10, 7, 8, 10]
```

Пример вывода: 40 '''

numbers = [10, 4, 5, 10, 7, 8, 10]
numb = 0

for num in numbers:
    if num < 10:
        numb += num
        
print(numb)

'''**Задача 4**

Есть список. Выведите, сколько в нем чисел 1 и 2 вместе

```python
numbers = [10, 4, 5, 1, 2, 10, 7, 8, 1, 2, 10]
```

Пример вывода: 4'''

numbers = [10, 4, 5, 1, 2, 10, 7, 8, 1, 2, 10]
count = 0

for num in numbers:
    if num == 1 or num == 2: ##### if num in [1,2]:
        count += 1
print(count)

'''**Задача 5**

Есть два списка. 

```python
numbers_1 = [1, 2, 3, 4, 5, 6, 7]
numbers_2 = [8, 9, 10, 11, 12]
```
Вычислите среднее в каждом списке (среднее это сумма деленная на количество). 

Выведите 

Первое среднее больше
или
Второе среднее больше
или
Средние одинаковые'''

numbers_1 = [1, 2, 3, 4, 5, 6, 7]
numbers_2 = [8, 9, 10, 11, 12]

sum1 = 0
sum2 = 0

for y in numbers_1:
    sum1 += y

for x in numbers_2:
    sum2 += x

sr1 = sum1 / len(numbers_1)
sr2 = sum2 / len(numbers_2)

print(sr1)
print(sr2)

if sr1 > sr2:
    print('Первое среднее больше')
elif sr1 < sr2:
    print('Второе среднее больше')
elif sr1 == sr2:
    print('Средние одинаковые')

'''**Задачка 6 – четные в списке**

У вас есть список слов

```python
letters = ["Alpha", "Bravo", "Charlie", "Delta", "Echo", "Foxtrot"]
```

Выведите в отдельном списке четные и отдельно нечетные элементы

Нечетные

Alpha
Charlie
Charlie

Четные

Bravo
Delta
Foxtrot'''

letters = ["Alpha", "Bravo", "Charlie", "Delta", "Echo", "Foxtrot"]
ch = []
nech = []

for let in range(len(letters)):
    if let % 2 == 0:
        ch.append(let)
    else:
        nech.append(let)

for i in ch:
    print(f'Нечетные {letters[i]}')
for t in nech:
    print(f'Четные {letters[t]}')

'''**Задача 7 - длина**

у вас есть список слов. Запишите в новый список длину каждого слова, выведите список

```python
letters = ["Alpha", "Bravo", "Charlie", "Delta", "Echo", "Foxtrot"]
```

Пример списка:

[5,5,7,5,4,7]
'''

letters = ["Alpha", "Bravo", "Charlie", "Delta", "Echo", "Foxtrot"]

len_let = []

for i in letters:
    len_let.append(len(i))
print(len_let)

'''**Задача 8 – гласные в списке**

У вас есть список гласных. 

Запишите в новый список встреченные согласные.

```python
letters = ["A", "B", "I", "O", "Q", "Z"]

vowels = ["A", "E", "I", "O", "U", "Y"]
```

Пример списка:

words = ["B", "Q", "Z"]'''

letters = ["A", "B", "I", "O", "Q", "Z"]

vowels = ["A", "E", "I", "O", "U", "Y"]

words = []

for letter in letters:
    if letter not in vowels:
        words.append(letter)

print(words)

'''**Задача 9 – range**
Пользователь вводит два целых числа. 
Заполните список четными числами, которые есть в промежутке. 
Оба числе не входят в промежуток

Ввод
1
5
Вывод
2
4
Ввод
5
10
Вывод
6
8'''

user_input1 = int(input())
user_input2 = int(input())

between = []

for i in range(user_input1, user_input2):
    if i %2==0:
        between.append(i)

for b in between:
    print(b)

'''**Задача 10 – range**

У вас есть список из чисел. 

Соберите список позиций (индексов) на которых расположены 0 и 1

```python
items = [0,1,2,3,1,2,4,1]
```

Пример вывода:

[0, 1, 4, 7]'''

items = [0,1,2,3,1,2,4,1]

ind_items = []

for i in range(len(items)):
    if items[i] in [0,1]:
        ind_items.append(i)

print(ind_items)

# Вывести все элементы списка кроме слов "Пропуск"

# Пример ответа:

# Желание Семнадцать Ржавый Печь

keywords = ["Желание", "Семнадцать", "Пропуск", "Ржавый", "Пропуск", "Печь"]
keywords_new = []

for key in keywords:  
    if key == "Пропуск": 
        continue
    else:
        keywords_new.append(key)

print(keywords_new)
# АЛЬТ решение: [keywords_new.append(key) for key in keywords if key != "Пропуск"]



# Телеграмма

# Превратите список в сообщение, замените "тчк" на "." "зпт" на "," 

# Пример ответа: 
# узнать, сделать, порадоваться.

list_w_spaces = ["узнать", "зпт", "сделать", "зпт", "порадоваться", "тчк"]
list = []

for i in list_w_spaces:
    if i == "зпт":
        list.append(',')
    elif i == "тчк":
        list.append('.')
    else:
        list.append(i)

print(' '.join(list))

# Игра в дартс
# Правила игры  такие: 
# Вы начинаете с 0 очков
# все очки, которые вы набрали складываются , но, если вы промахнулись 
# (набрали 0), то теряете 10 за первый раз, 20 за второй 30 за 3 и так далее
# Есть список бросков, узнать сумму 

throws = [5, 3, 2, 10, 5, 0, 5, 20, 0, 10]
points = 0
attempts = 0

for i in throws:
    if i == 0:
        attempts += 10
        points -= attempts
    else:
        points += i

print(points)

# В доме живут жители от 0 до 99 лет, вычислите средний возраст
# Пример ответа: 
# 15

residents = [5, 3, 2, 20, 5, 30, 5, 40, 17]
sum = 0

for i in residents:
    sum += i
sr_age = sum / len(residents)

print(round(sr_age))

### Задачки на range
'''На `for i in range()`

# Вывести список из 8 степеней числа 2
a = 2
# пример ответа
1 2 4 8 16 32 64 128
```'''
a = 2
for z in range(8):
    t = z**a
    print(t)

b = [a**i for i in range(8)]
print(b)

'''# Вывести список всех чисел меньше 120, в которых присутствует цифра 1
# пример ответа
1 10 11 21 31 41 51 61 71 81 91 100 101 110 111 '''

for i in range(120):
    if '1' in str(i):
        print(i)

'''### На `for i in range() и индексы`
# Задача 1
# позиции нулей
# Вывести все позиции на которых стоят нули
sequence = [0, 1, 1, 0, 1, 0, 0, 1]
# пример ответа
0
3
5
6'''

sequence = [0, 1, 1, 0, 1, 0, 0, 1]
pos = []

for item in range(len(sequence)):
    if sequence[item] == 0:
        pos.append(item)

print(pos)

'''# Инверсия
# С помощью цикла выведите список в обратном порядке
Пример ответа:
# Foxtrot Echo Delta Charlie Bravo Alpha'''

letters = ["Alpha", "Bravo", "Charlie", "Delta", "Echo", "Foxtrot"]
len_let = 0
let_inv = []
for i in range(len(letters), 0, -1):
    let_inv.append(i-1)   # ______len берет реальную длинну т.е. (6), поэтому (i-1)______

for count in let_inv:
    print(letters[count])
#________________ещё вариант________________________________________
#[let_inv.append(i-1) for i in range(len(letters), 0, -1)]
#[print(letters[count]) for count in let_inv]
    

'''# Вывести пары слов из 2 списков в формате "Слово" – "Перевод"
en = ["Cat", "Dog", "Owl"]
ru = ["Котейка", "Собаня", "Совуня"]
Пример ответа:
Cat – Котейка
Dog – Собаня
Owl – Совуня'''

en = ["Cat", "Dog", "Owl"]
ru = ["Котейка", "Собаня", "Совуня"]

for i in range(len(en)):
    print(en[i], '-', ru[i])

### Задачки на while

'''# Спрашивайте сделал ли пользовтель домашку, пока он не скажет да
# Пример ответа:
Ты сделал домашку?
> Нет
Ты сделал домашку?
> Угу
Ты сделал домашку?
> Да
Какой ты молодец"'''

print('Ты сделал домашку?: ')

while True:
    user_input = input()
    if user_input == 'Да':
        print('Какой ты молодец')
        break
    else:
        print('Ты сделал домашку?: ')

'''# Досчитайте от 1 до 5 с помощью while
# Пример ответа:
1
2
3
4
5'''

i = 0

while i < 5:
    i += 1
    print(i)

'''# Спрашивайте у пользователя (с помощью input() ) ввод пока он не введет "хватит"
# и записывайте каждое полученное значение в список shopping_list
# Когда пользователь набрал "хватит", выведите список, например:

Яблочки
Сыр
Бумага для принтера'''

list = []
while True:
    i = input('Ввод: ')
    if i == "хватит":
        break
    else:
        list.append(i)
    print(list)

