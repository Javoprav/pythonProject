tasks_all = 150 # процент
tasks_solved = 30
task_percent = tasks_solved / tasks_all * 100
task_percent_round = round(task_percent)
# Округляем до целого
print(task_percent_round)
# Вернет 20


# найти количество процентов от числа
price = 3000
percent = 20

# Сперва приводим процент к дроби:
fracture = percent / 100 # получится 0.2

# Затем умножаем цену на дробь
discounted = price * fracture
# Выводим результат
print(discounted)
# Будет выведено 600.0


# вычислить цену со скидкой, если известна цена и скидка.
price = 3000
discount = 20

# Сперва приводим процент к дроби:

fracture = discount / 100 # получится 0.2

# Затем вычитаем из цены сумму скидки

price_discounted = price - price * fracture

# Выводим результат

print(price_discounted)
# Выведет 2400.0

П# утем несложных математических операций можно сократить так:

price = 3000
discount = 20

price_discounted = price * (1 - discount / 100)

print(price_discounted)

# Выведет 2400.0
# И последний пример — увеличение суммы на процент. Например, увеличение депозита после получения процента по вкладу.

deposit = 5000
interest = 10

interest_frac = interest / 100

deposit_new = deposit + deposit * interest_frac

print(deposit_new)

# Выведет 5500.0
# Путем несложных математических операций можно сократить так:

deposit = 5000
interest = 10

deposit_new = deposit * ( 1 + interest / 100 )

print(deposit_new)

# Выведет 5500.0
Минимум, максимум и среднее
Для частых операций у Python есть специальные функции.

# Функция
min(число, число, число, ...)
#  вычисляет минимальное значение, например:

result = min(5, 4, 3, 2, 1)
print(result)

# Выведет 1
# Функция
max(число, число, число, ...)
#  вычисляет максимальное значение, например:

result = max(5, 4, 3, 2, 1)
print(result)

# Выведет 5
# Мы можем часто услышать о средней зарплате, среднем времени ожидания или среднем количестве друзей. Чтобы вычислить среднее, нужно сложить все числа и поделить на их количество. Например, так:

total = 5 + 4 + 3 + 2 + 1  # total - всего
average = total / 5 # average - среднее
print(average)

# Выведет 3

