first_set = {'Alex', 'John', 'Georg', 'Alex', 'Tom'}
print(type(first_set))
print(first_set)
print(len(first_set))
first_set.add('Maxim') # добавляет значение в множество
print(first_set)
print('Maxim' in first_set)
first_set.remove('Alex') # удаление элемента
print(first_set)
# first_set.clear() # очищает множество
second_set = {'Anton', 'Tom', 'Anna', 'Alex'}
third_set = first_set.union(second_set) # объединяет множества
print(third_set)
fourth_set = first_set.intersection(second_set) # выводит пересечения во множетсвах
print(fourth_set)
fifth_set = first_set.difference(second_set) # ищем в первом сете значения которые есть во втором
print(fifth_set)
print(fifth_set - second_set)
set1 = {1,2,3}
set2 = {1,2,3,4,5}
print(set1.issubset(set2)) # является ли подмножеством set1
print(set2.issuperset(set1)) # является ли наддмножеством set1
# print(set1[0]) # тип set не поддерживает обращение к элементу по индексу