print ("Привет, мир!")
print ("Привет вновь!")
print ("Мне нравится это печатать.")
print ("Ура! Я печатаю!")
print ('Это весело!')
print ("3TO занятие как 'волшебство'.")
print ('H бы "сказал", что это круто!')

print('Я подсчитаю свою живность')
print('Куры', 25 + 30 / 6)
print("Петухи", 100 - 25 * 3 % 4)
print("А теперь я подсчитаю яйца:")
print(3+2+1-5+4%2-1/4+6)
print("Верно ли, что  3 + 2 < 5 - 7?")
print(3 + 2 < 5 - 7)
print('Сколько будет  3 + 2?', 3 + 2)
print("А сколько будет 5 - 7", 5 - 7)
print("Эот больше", 5 > -2)
print('А это больше или равно?', 5 >= -2)
print('А это меньше или равно', 5 <= - 2)
# 3
cars = 100
space_in_a_car = 4.0
drivers = 30
passenders = 90
cars_not_driven = cars - drivers
cars_driven = drivers
carpool_capacity = cars_driven * space_in_a_car
average_passenfers_per_car = passenders / cars_driven

print('В наличии', cars, "автомобилей")
print("И только", drivers, "влдителей вышли на работу")
print("Получается что", cars_not_driven, "в машин пустует")
print("Мы можем перевезти сегодня", carpool_capacity, 'человек')
print("Сегодня нужно отвезти", passenders, 'человек')
print("В каждой машине будет примерно", average_passenfers_per_car, "человека")
# 5
my_name = "Макс"
my_age = 35 # это правда
my_height = 178 # см
my_weight = 70 #
my_eyes = 'зеленые'
my_teeth = 'белые'
my_hair = "каштановые"

print(f"Давайте поговорим о человеке по имени {my_name}")
print(f"Его рост составляет {my_height}")
print(f"Он весит {my_weight}")
print("На самом деле это не так и много")
print(f"У него {my_eyes} глаза и {my_hair} волосы")
print(f"Его зубы обычно {my_teeth}, хотя он и любит пить кофе.")
total = my_age + my_height + my_weight
print(f"Если я сложу {my_age}, {my_height} и {my_weight}, то получу {total}")

rasst = 30 # km
rasst_m = (rasst * 1000)
print("Расстояние в метрах", rasst_m)

types_of_people = 10
x = f"Существует {types_of_people} типов людей"
binary = 'Python'
do_not = 'Нет'
y = f'Те, кто понимает {binary}, и те, кто - {do_not}.'
print(x)
print(y)
print(f'Я сказал: {x}')
print(f"А ещё я сказал: {y}")
Hilarious = False
joke_evalution = "Разве это смешно?! {}"
print(joke_evalution.format(Hilarious))

w = "Эта часть строки слева..."
e = "а это справа"
print(w + e)

print("У Мэри был маленький барашек.")
print("Его шерсть была белой как {}.".format('снег')) # фигурные ковычки добавляют слово через .format
print("И всюду куда Мэри шла,")
print("Маленький барашек всегда следовал за ней.")
print("." * 10) # что это могла значить?

end1 = "Б"
end2 = "а"
end3 = "д"
end4 = "д"
end5 = "и"
end6 = "Г"
end7 = "а"
end8 = "й"
print(end1 + end2 + end3 + end4 + end5, end = ' ')
print(end6 + end7 + end8)

formatter = "{} {} {} {}"
# 8
print(formatter.format (1,2,3,4))
print(formatter.format("раз", "два", "три", "четыре"))
print(formatter.format(True, False, False, True))
print(formatter.format(formatter, formatter, formatter,formatter))
print(formatter.format(
    "Спят в конюшне пони\n",
    "начал пес дремать",
    "только мальчик джонни",
    "хочет всех послать!"
))

# 9
days = "Пн Вт Ср Чт Пт Сб Вс"
months = "\nЯнв\nФевр\nМарт\nАпр\nМай\nИюнь\nИюль\nАвг"
print("Это дни недели: ", days)
print("А это месяцы: ", months)
print("""
Что?
Используются три двойние ковычки.
Мы можем набрать текста сколько угодно.
много строк
""")

# 10

d_artanan = "\tМеня зовут д'Артанян"
print(d_artanan)
