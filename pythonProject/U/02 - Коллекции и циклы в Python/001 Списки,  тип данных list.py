new_list = [1, 2, 3, 4]
mix_list = [12, 3.14, 'text']
print(len(new_list)) # len длинна списка
print(new_list[0]) # выводит нулевой символ
print(new_list[2:]) # делает срез от 2 символа и далее
list_1 = ['anna', 'Alex', 'Max']
list_2 = ['john', 'nicolas', 'vlad']
print(list_1 + list_2) # соединение списков
list_1[0] = 'artur' # меняет нулевую строку
print(list_1)
list_1.append('Anna') # добавление строки
print(list_1)
list_1.insert(1, 'John') # добавляет на 1 строку новое значение
print(list_1)
print(list_1.index('Max')) # показывает позицию строки
list_1.index('Max', 0, 10) # показывает позицию строки и с какой строки по какую искать
pop_del = list_1.pop()
print(pop_del)
list_1.pop(0) # удаление элемента 0
print(list_1)
list_1.clear() # очистка листа
list_3 = ['33', '22', '11', '44']
print(list_3)
list_3.sort() # сортирует список поочередно
print(list_3)
list_3.sort(reverse=True) # аргумент меняет функцию списка в обратном порядке
print(list_3)
list_4 = ['abcde', 'bcb', 'da', 'cde', 'ser', 'q']
print(list_4)
list_4.sort() # сортировка
print(list_4)
list_4.sort(key=len) # сортировка по длинне символов
print(list_4)
list_4.reverse() # отображает список в обратном порядке
print(list_4)