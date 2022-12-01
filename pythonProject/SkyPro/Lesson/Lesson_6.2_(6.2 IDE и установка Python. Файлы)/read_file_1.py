file_1 = open('text_1.txt', 'rt') #  r - read (чтение), t - text (текст)

count_guest = 0

with open('text_1.txt', 'rt') as file_1:  # что бы не закрывать файл

    for name in file_1:
        print(name)
        count_guest += 1
# count_guest_1 = len(file_1.readlines()) № выводит кол-во строк в файле
print(f'Кол-во футболистов: {count_guest}')
print(f'Кол-во футболистов: {count_guest_1}')