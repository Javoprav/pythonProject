i = 10
if i > 1:
 i = i - 1
 print(i)

i = 1
if i > 1:
 i = i - 1
 print(i)
elif i == 1:
 i = (i + 1) * 3 + 1
 print(i)

i = int(-3)
if i > 1:
 i = i - 1
 print(i)
elif i == 1:
 i = i + 1
 print(i*2)
else:
 print(i**2)

i = 25
if i <= 0:
 print(i)
elif i < 0:
   i = i - 10
   if i <= 0:
    print(i)
   elif i > 0:
      i = i - 10
      if i <= 0:
       print(i)
else:
 print('error')

i = 10
if i > 1 and i < 10:
 i = i - 1
 print(i)
elif i == 1 or i == 10:
 i = i + 1
 print(i)
print(i + 1)

i = 4
if i > 1 and i < 10:
 i = i * 2
 print (i)
 if i > 1 and i < 10:
  i = i * 2
  print (i)
  if i > 1 and i < 10:
   print (i * 2)
  else:
   print (i + 2)
 else:
  print (i + 2)
else:
 print(i)

""" i = int(input())
if i > 1:
  i = i - 1
  print(i)
elif i == 1:
  i = (i + 1)*3) + 1  -  D. Количество открытых скобок не равно количеству закрытых.
  print(i) """

"""a = float(input("a = "))
sum = a + b 
if sum > 10:
 i = 'Try again'
 print(i)                  А. Переменная не определена."""

"""i = 10
if i > 1 and i < 10:
 i = i - 1
 print(i)
elif i = 1 or i = 10:     H. Неверный оператор сравнения.
 i = i + 1
 print(i)
print(i+1)"""

"""i = '5'
if i > 1:
 a = input('a = ')
 i = i + a
 print(i)
elif i == 1:
 b = input('a = ')    B. Невозможное присваивание.
 i = i + b
 print(i)
else:
 print(i*2)"""

"""i = int(input(Введите число))  D. Количество открытых скобок не равно количеству закрытых.
if i <= 0:
 print(i)
elif i > 0:
 i = i - 10
 if i <= 0:
  print(i)
 elif i > 0:
  i = i - 10
  if i <= 0:
   print(i)
  else:
   print('error')"""

""""# 7.6
c = input("a = ")   E. Невозможная операция сложения/конкатенации.
i = c + 3
if c > 1:
 i = i - 1
 print(i)
elif c == 0:
 i = i + 1
 print(i)"""

"""i = 25
if i <= 0:
print(i)      G. Отсутствие отступа.
elif i > 0:
i = i — 10
if i <= 0:
print(i)
elif i > 0:
i = i - 10
if i <= 0:
print(i)
else:
print('error')"""

"""i = 4
if i > 1 and i < 10:
 i * 2 = i             F. Невозможная операция сравнения.
 print (i)
 if i > 1 and i < 10:
  i * 2 = i
  print (i)
  if i > 1 and i < 10:
   print (i*2)
  else:
   print (i+2)
 else:
  print (i+2)
else:
 print(i)"""

