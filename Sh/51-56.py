"""# 8. Напишите программу, которая вычисляет произведение
двух целых чисел, введенных с клавиатуры, но выводит его три
раза. Используйте в задаче функции преобразования типов int()
и str().
Пример:
Введите первое число: 5
Введите второе число: 10
505050 """

a = int(input('просит пользователя ввести число: '))
b = int(input('просит пользователя ввести число: '))
c = a*b
print(str(c)*3)

"""9. Напишите программу, которая выводит строку, введенную
пользователем с клавиатуры, столько раз, сколько запросил
пользователь.
Пример:
Введите строку: ма
Введите количество повторений: 2
мама"""

a = input('Введите строку: ')
b = int(input('Введите количество повторений: '))
print(a*b)

'''Напишите программу, которая просит пользователя ввести
сообщение и выводит его с комментарием для другого человека.
Пример:
Введите сообщение: Это Ольга, ваш новый менеджер.
Для вас одно новое сообщение: "Это Ольга, ваш новый
менеджер."'''

a = input('Введите сообщение: ')
print('Для вас одно новое сообщение: ', a)

'''11. Напишите программу, которая запрашивает количество по-
купаемых продуктов и выводит общую стоимость покупки. Ис-
пользуйте следующую таблицу стоимости продуктов:
хлеб — 35.5 руб. молоко — 74 руб. масло — 120 руб.
Пример:
Количество покупаемых единиц хлеба: 1
Количество покупаемых единиц молока: 2
Количество покупаемых единиц масла: 0
Общая сумма к оплате - 183.5 руб.'''

h = 35.5
m = 74
ma = 120
h1 = int(input('Количество покупаемых единиц хлеба: '))
m1 = int(input('Количество покупаемых единиц молока: '))
ma2 = int(input('Количество покупаемых единиц масла: '))
h2 = float(h*h1)
m2 = float(m*m1)
ma3 = float(ma*ma2)
print('Общая сумма к оплате - ', h2+m2+ma3)

print('Есть ли у Вас дисконтная карта нашего магазина?')
X = input("1 - 'Да'; 0 — 'Не помню'; -1 — 'Нет': ")
if X == '1':
 print('Приложите карту к терминалу')
elif X == '0':
 print('Проверить наличие Вас в базе данных?')
elif X == '-1':
 print('Вы хотели бы приобрести дисконтную карту?')

print('Есть ли у Вас дисконтная карта нашего магазина?')
X = input("1 - 'Да'; 0 - 'Не помню'; -1 - 'Нет': ")
if X == '1':
 print('Приложите карту к терминалу')
elif X == '0':
 print('Проверить наличие Вас в базе данных?')
X = input("1 - 'Да'; -1 - 'Нет': ")
if X == '1':
 print('Обратиться по поводу восстановления номера карты можно к администратору магазина')
elif X == '-1':
 print('Можете продолжить покупку')
elif X == '-1':
 print('Вы хотели бы приобрести дисконтную карту?')
X = input("1 - 'Да'; -1 - 'Нет': ")
if X == '1':
 print('Обратиться по поводу приобретения дис-
контной карты можно к администратору магазина')
elif X == '-1':
print('Можете продолжить покупку')