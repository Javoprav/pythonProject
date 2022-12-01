my_dict = {"name" : "Max", "age" : 35}
print(my_dict)
mydict = dict(Name="Maxim", Age=35, isMale=True)
print(mydict)
print(mydict["Age"])

print("\n-----------------------\n")

for key in mydict:
    print(key, " = ", mydict[key])

my_tuple = ('Name', 'Age', 'isMale')
for key1 in my_tuple:
    print(key1, ' = ', mydict[key])

print("\n-----------------------\n")

mydict2 = {i * 2: i for i in range (1,10)}
print(mydict2)
print(mydict2[2])

mydict3 = {str(i * 2): i for i in range (1,10)}
print(mydict3)

print("\n-----------------------\n")

'''1) Создайте словарь с двумя ключами «Name» и «Age» и значениями «Без имени» и «-1».
2) Попросите пользователя ввести своё имя.
3) Попросите пользователя ввести свой возраст.
4) Примите эти данные и измените соответствующие элементы словаря.
5) Выведите этот словарь (ключи и значения), используя цикл for.'''

mydict4 = {'Name' : 'Без имени', 'Age' : -1}
name = input('ввести своё имя = ')
age = input('ввести свой возраст = ')
mydict4 = {'Name' : (name), 'Age' : (age)}
print(mydict4)
for x in mydict4:
    print(x)
    print(x, " = ", mydict4[x])