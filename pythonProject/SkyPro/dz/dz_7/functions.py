'''импорты и переменные'''
import os
import json

stud = os.path.join('data', 'students.json')
profi = os.path.join('data', 'professions.json')

'''Загружает список студентов из файла'''


def load_students_prof(student):
    with open(stud, 'r', encoding='utf-8') as f:
        data1 = json.load(f)
        for i in data1:
            if i["full_name"].lower() == student.lower():
                student_list = i["skills"]

    return student_list


'''Загружает список профессий из файла'''


def load_professions(x):
    with open(profi, 'r', encoding='utf-8') as f:
        data2 = json.load(f)
        for i in data2:
            if i["title"].lower() == x.lower():
                return_2 = ''
                break
            else:
                return_2 = 'У нас нет такой специальности'
    return return_2


'''Получает словарь с данными студента по его pk'''
'''def get_student_by_pk(pk):
    with open(stud, 'r', encoding='utf-8') as f:
        data3 = json.load(f)
        for i in data3:
            if i["pk"] == int(pk):
                skl = ' '.join(i["skills"])
                break
    return skl'''


def get_student_by_pk(pk):
    return_1 = ''
    with open(stud, 'r', encoding='utf-8') as f:
        data3 = json.load(f)
        for i in data3:
            if i["pk"] == int(pk):
                student = i["full_name"]
                skl = ' '.join(i["skills"])
                return_1 = f'Студент {student}\nЗнает {skl}'
                break
            else:
                return_1 = 'У нас нет такого студента'

    return return_1


'''Получает словарь с инфо о профе по названию'''


def get_profession_by_title(title):
    with open(profi, 'r', encoding='utf-8') as f:
        data4 = json.load(f)
        for i in data4:
            if i["title"].lower() == title.lower():
                fitness = i["skills"]
                # student = i["full_name"]
                # skl = i["skills"]
    return fitness


'''функция, которая получив студента и профессию, возвращает словарь'''


def check_fitness(student_set, profession_set):
    has = profession_set.intersection(student_set)
    lacks = profession_set.difference(student_set)

    has_list = list(has)
    lacks_list = list(lacks)

    has_list_len = len(has_list)
    lacks_list_len = len(lacks_list)

    task_percent = has_list_len / lacks_list_len * 100

    estimation = {"has": has_list, "lacks": lacks_list, "fit_percent": int(task_percent)}

    return estimation