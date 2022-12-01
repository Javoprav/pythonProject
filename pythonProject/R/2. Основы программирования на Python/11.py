import random
print(random.random())
print(random.random() * 10)
print(int(random.random() * 10))

my_set = set("Pythonnnnnnnnnnnnnn")
print(my_set)

list1 = [i for i in range(1,10)]
print(list1)
set1 = set(list1)
print(set)

list2 = [int(random.random() * 10) for i in range(1,10)]
print(list2)

list3 = [int(random.random() * 10) for x in range(0,10)]
print(list3)
list4 = list(set(list3))
print(list3)

'''1) Попросите пользователя ввести количество элементов для списка.
2) Создайте список, состоящий из целых случайных чисел от 0 до 100, заданного пользователем количества.
3) Выведите этот список с помощью цикла while.
4) С помощью множеств удалите из списка все повторяющиеся значения.
5) Выведите получившийся список с помощью цикла for.'''

y = int(input('ввести количество элементов для списка = '))
li = [int(random.random() * 10) for z in range(0,y)]
print(li)
u = 1
while u < 1:
    u += 1
    print(li)
li2 = list(set(li))
print(li2)
for q in li2:
    print(q)