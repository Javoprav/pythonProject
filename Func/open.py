# Чтение данных из файлов
# открытие файла
file = open("filename.txt", "r")

cont = file.read()

print(cont)

file.close()