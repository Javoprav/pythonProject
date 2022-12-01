'''1) Узнайте, какое исключение появляется при делении числа на 0.
2) Попросите пользователя ввести 2 числа.
3) Выведите результат деления.
4) Перехватите исключение при делении на 0 и выведите пользователю в качестве результата слово «бесконечность».'''

# a = 88/0
# print(a)
while True:
    x = int(input('Введите число 1: '))
    y = int(input('Введите число 2: '))
    try:
     z = x / y
    except ZeroDivisionError:
     print('Бесконечность')
    else:
     print(z)
    finally:
        print('В любом случае завершаем программу...')
        exit(0)
        
"""  if z <= 0:
         raise Exception('Число не положительное')
    except ValueError:
     print('Не возможно привести к числу')
    except Exception as exp:
        print(exp)
    else:
        print('Спасибо за корректный ввод')
    finally:
        print('В любом случае завершаем программу...')
        exit(0)

try:
    z = float(z)
except ZeroDivisionError:
    print('Бесконечность')
print(z)
"""

