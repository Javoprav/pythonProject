from functions import load_students_prof, load_professions, get_student_by_pk, get_profession_by_title, check_fitness
import os
import json
stud = os.path.join('data', 'students.json')
profi = os.path.join('data', 'professions.json')
student = ''

print('Введите номер студента: ')
user_input_pk = input()

print(get_student_by_pk(user_input_pk))

with open(stud, 'r', encoding='utf-8') as f:
    data3 = json.load(f)
    for i in data3:
        if i["pk"] == int(user_input_pk):
            student = i["full_name"]

if get_student_by_pk(user_input_pk) == 'У нас нет такого студента':
    quit()

user_input_prof = input(f'Выберите специальность для оценки студента {student}: ')

prof_request = user_input_prof.lower()

if load_professions(prof_request) == 'У нас нет такой специальности':
    quit()

students_prof_list = set(load_students_prof(student))
profession_by_title_list = set(get_profession_by_title(prof_request))

final_dict = check_fitness(students_prof_list, profession_by_title_list)
pr = final_dict['fit_percent']
has = final_dict['has']
lacks = final_dict['lacks']
str_has = ' '.join(has)
lacks_str = ' '.join(lacks)

print(f'Пригодность {pr}% \n{student} знает {str_has} \n{student} не знает {lacks_str}')