def get_grade(grade):
    if grade == 2:
        return ("Плохо")
    elif grade == 3:
        return ("Удовлетворительно")
    elif grade == 4:
        return ("Хорошо")
    elif grade == 5:
        return ("Отлично")
    else:
        return ("Ошибка")

# Код вашей функции должен быть выше

try:
    assert get_grade(2) == "Плохо"
    assert get_grade(3) == "Удовлетворительно"
    assert get_grade(4) == "Хорошо"
    assert get_grade(5) == "Отлично"
    assert get_grade("") == "Ошибка"
except AssertionError:
    print("Неверно, проверьте функцию на разных значениях")
else:
    print("Все хорошо, все работает")