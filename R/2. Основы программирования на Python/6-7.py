print('Введите 0, 1 или 2:')
a = input()
if a == "0":
    print('Вы ввели 0')
    if 5 == 5:
     print ("5 = 5")
    else:
        print (5!=5)
elif a == '1':
    print('Вы ввели 1')
elif a == '2':
    print('Вы ввели 2')
else:
    print('Не корректный ввод...')
print('Это число меньше 10')

cond = a == '0' or a == '1' or a == '2' # cond присваивается значение в зависимости от ввода input

if cond:
    x = 0
else:
    x = 3
print ('x =', x)

x = 0 if cond else 3 # то же что и предыдущий код

print('Введите 3 числа:')
a = int(input())
b = int(input())
c = int(input())
d = a + b + c
print ("Cреднее арифметическое этих чисел", d / 3)