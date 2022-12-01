s = 'abc' 
t = [10, 20, 30]

# {'a': 10, 'b': 20, 'c': 30}

dict_st = {}
for i in range(3):
    dict_st[s[i]] = t[i]
print(dict_st)
# or zip
print(dict(zip(s,t)))


matrix = [[1, 2, 3], [1, 2, 3]] # Как транспонировать эту матрицу?
matrix_T = [list(i) for i in zip(*matrix)]


id = [1, 2, 3, 4]
leaders = ['Elon Mask', 'Tim Cook', 'Bill Gates', 'Yang Zhou']
record = zip(id, leaders)

print(list(record))
# [(1, 'Elon Mask'), (2, 'Tim Cook'), (3, 'Bill Gates'), (4, 'Yang Zhou')]


id = [1, 2, 3, 4]
record = zip(id)
print(list(record))
# [(1,), (2,), (3,), (4,)]

'''Python и здесь придёт на помощь. В модуле itertools есть функция zip_longest. Посмотрим, как с её помощью генерируется список record:'''

from itertools import zip_longest
id = [1, 2]
leaders = ['Elon Mask', 'Tim Cook', 'Bill Gates', 'Yang Zhou']

long_record = zip_longest(id, leaders)
print(list(long_record))
# [(1, 'Elon Mask'), (2, 'Tim Cook'), (None, 'Bill Gates'), (None, 'Yang Zhou')]

long_record_2 = zip_longest(id, leaders, fillvalue='Top')
print(list(long_record_2))
# [(1, 'Elon Mask'), (2, 'Tim Cook'), ('Top', 'Bill Gates'), ('Top', 'Yang Zhou')]


                                  # Распаковывание

record = [(1, 'Elon Mask'), (2, 'Tim Cook'), (3, 'Bill Gates'), (4, 'Yang Zhou')]
id, leaders = zip(*record)
print(id)
# (1, 2, 3, 4)
print(leaders)
# ('Elon Mask', 'Tim Cook', 'Bill Gates', 'Yang Zhou')


id = [1, 2, 3, 4]
leaders = ['Elon Mask', 'Tim Cook', 'Bill Gates', 'Yang Zhou']

# создаём словарь, используя «dict comprehension»
leader_dict = {i: name for i, name in zip(id, leaders)}
print(leader_dict)
# {1: 'Elon Mask', 2: 'Tim Cook', 3: 'Bill Gates', 4: 'Yang Zhou'}

# создаём словарь, используя функцию «dict»
leader_dict_2 = dict(zip(id, leaders))
print(leader_dict_2)
# {1: 'Elon Mask', 2: 'Tim Cook', 3: 'Bill Gates', 4: 'Yang Zhou'}

# обновляем
other_id = [5, 6]
other_leaders = ['Larry Page', 'Sergey Brin']
leader_dict.update(zip(other_id, other_leaders))
print(leader_dict)
# {1: 'Elon Mask', 2: 'Tim Cook', 3: 'Bill Gates', 4: 'Yang Zhou', 5: 'Larry Page', 6: 'Sergey Brin'}


'''надо вычислить разницу между соседними числами.'''

numbers = [12, 3, 7, 15, 8]
diff = [a-b for a, b in zip(numbers, numbers[1:])]
result: [9, -4, -8, 7]


'''сортировка списков'''

list1 = [3,2,4,1, 1]
list2 = [‘three’, ‘two’, ‘four’, ‘one’, ‘one2’]
list1, list2 = zip(*sorted(zip(list1, list2)))
# (1, 1, 2, 3, 4)
# (‘one’, ‘one2’, ‘two’, ‘three’, ‘four’)


'''вместе с циклами for.'''

products = ["cherry", "strawberry", "banana"]
price = [2.5, 3, 5]
cost = [1, 1.5, 2]
for prod, p, c in zip(products, price, cost):
    print(f'The profit of a box of {prod} is £{p-c}!')
# Прибыль от одного ящика вишни составляет 1,5 фунта!
# Прибыль от одного ящика клубники составляет 1,5 фунта!
# Прибыль от одного ящика бананов составляет 3 фунта!

'''Как транспонировать матрицу?'''

matrix = [[1, 2, 3], [1, 2, 3]]
matrix_T = [list(i) for i in zip(*matrix)]
print(matrix_T)
# [[1, 1], [2, 2], [3, 3]]

