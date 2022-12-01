grades = {2:"Плохо", 3:"Удовлетворительно", 4:"Хорошо", 5:"Отлично"}

def get_grade(grade):
    return grades[grade]

# Не удаляйте код ниже, он нужен для вызова функции и проверки

grade = int(input())
print(get_grade(grade))