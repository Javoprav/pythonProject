def sum(x,y):
 return x + y
s = sum(5, 7)
print(s)

def sub(x,y):
 return x - y
print(sub(10, 15))
print(sub(10, 5))
print(sub(y=10, x=5))

def su(x, y, r=False):
 a = sum(x, y)
 if r:
     return a
 else:
  print(a)
su(15, 7)
su(15, 7, True)
print(su(15, 7, True))

def bigsum(*numbers):
 t = 0
 print(numbers)
 for m in numbers:
  t += m
 return t
print(bigsum(1, 5, 7, 0, 1))

def printdict(**dict):
 for key in dict:
     print(key, '=', dict[key])
printdict(name='Alex', age=15)

lambdafunc = lambda x, y: print(x + y)
lambdafunc(5 , 7)

'''1) Создайте функцию, которая проверяет чётное число передано в параметре или нет. Она должна возвращать True или False.
2) Создайте функцию, которая принимает список и возвращает максимальное значение из списка.
3) Создайте функцию с переменным числом аргументов, внутри которой должно выводиться среднее арифметическое переданных чисел.
Примечание: среднее арифметическое чисел равно сумме этих чисел поделённое на их количество.'''


def num(x):
 if x % 2 == 0:
  print(True)
 else:
  print(False)
num(5)
num(6)

print("\n-----------------------\n")

def list1(*list):
    print(max(list))
list1(1, 5, 7, 0, 1)

print("\n-----------------------\n")

def num(x, y):
    print (x + y / 2)
num(2, 8)