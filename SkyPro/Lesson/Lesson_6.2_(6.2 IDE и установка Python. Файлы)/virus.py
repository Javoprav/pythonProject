
virus_code = 'print("я вирус")'

with open('shopping_list_copy.py', 'a') as file:
    file.write(f'\n{virus_code}\n')