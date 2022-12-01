with open('students.txt') as file:
    for student_data in file:
        # data = student_data.rstrip('\n').split(':') # rstrip() удаляет указанный символ справа,
        # пустой strip удаляет последний символ,
        # name = data[0]
        # language = data[1]

        name, language = student_data.rstrip('\n').split(':')

        print(f'{name} учит {language}!')