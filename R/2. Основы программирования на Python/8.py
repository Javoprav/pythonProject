i = 0
while i < 10:
    i += 1
    print ('Hey')
print('Цикл завершен')

i = 0
while i < 10:
    i += 1
    if i == 5:
        continue
    print (i)
print('Цикл завершен')

i = 0
while i < 10:
    i += 1
    if i == 5:     # пропуск 5 
        continue
    if i == 8:     # стоп на 8
        break
    print (i)
print('Цикл завершен')

a = 0
to = 10
x = 1
while x <= to:
    a += x
    x += 1
print('Сумма чисел от 1 до ', to, 'равна ', a )

while True:
    c = input('Введите 0 для выхода ')
    if c == '0':
        break