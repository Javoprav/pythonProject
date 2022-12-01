'''17. Напишите программу, которая вычисляет факториал неотрицательного числа,
введенного с клавиатуры, и выводит
ошибку, если пользователь ввел отрицательное число.
Факториал числа n (n!) — это произведение натуральных чисел от 1 до n.
Например, 5! * 1 * 2 * 3 * 4 * 5 *. При этом 0! = 1.'''

'''x = int(input("Факториал числа n (n!): "))
for y in range(1, x + 1):
    x += 1 * x
    if x < 0:
        print ('Ошибка')
    print(x)

x = int(input("Факториал числа n (n!): "))
y = 0
while y < x:
 y += 1
 y = y * y
 if x < 0:
  print ('Ошибка')
print(y)'''


n = int(input('Факториал числа: '))
factorial = 1
while n > 1:
    factorial *= n
    n -= 1
print('= ', factorial)

n = int(input('Факториал числа: '))
factorial = 1
for i in range(2, n+1):
    factorial *= i
if n < 0:
 print('ошибка')
else:
 print(factorial)

def fac(n):
    if n == 0:
        return 1
    return fac(n-1) * n
print(fac(5))