"""Разработка
13. Напишите программу, которая подсчитывает количество
ячеек в таблице, содержащей 5 строк и 2 столбца. При этом:
13.1) внешний цикл проходит все ячейки таблицы по столбцам;
13.2) внешний цикл проходит все ячейки таблицы по строкам."""
"""count = 0
for str in range(1,4):
 for stolb in range(1,5):
  count = count + 1
print(count)"""

count = 0
for str in range(1,6):
 for stolb in range(1,3):
  count = count + 1
print(count)

count = 0
for stolb in range(1,3):
 for str in range(1,6):
  count = count + 1
print(count)

"""14. С помощью цикла for:
14.1) выведите на экран числа от 25 до 50;
14.2) выведите на экран только четные числа из диапазона
от 25 до 50;
14.3) выведите на экран все нечетные числа от 25 до 50,
кроме тех, что больше 45, с помощью директивы continue."""
y = 24
for x in range(25,51):
 y += 1
 print(y)

y = 24
for x in range(25,51):
 y += 1
 if y % 2 == 0:
  print(y)

y = 24
for x in range(25,51):
 y += 1
 if y % 2 == 1:
  if y >= 45:
   continue
  print(y)