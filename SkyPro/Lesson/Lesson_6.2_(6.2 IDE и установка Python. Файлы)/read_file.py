file = open('text.txt', 'rt') #  r - read (чтение), t - text (текст)

# content = file.read(6) # 6 это кол-во байт текста или файла. read - считывание файла
# print(content) # Выведет: Hellow

# for i in file:
#     print(i)

# file.close() # закрывает файл

with open('text.txt', 'rt') as file:  # что бы не закрывать файл
    for i in file:
     print(i)

file_1 = open('text_1.txt', 'rt') #  r - read (чтение), t - text (текст)

count_guest = 0

with open('text_1.txt', 'rt') as file_1:  # что бы не закрывать файл
    count_guest_1 = len(file_1.readlines())
    for name in file_1:
     print(name)
     count_guest += 1

print(f'Кол-во футболистов: {count_guest}')
print(f'Кол-во футболистов: {count_guest_1}')