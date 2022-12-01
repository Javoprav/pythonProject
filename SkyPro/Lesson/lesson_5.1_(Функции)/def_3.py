def get_percent_rounded(a, b):
    return f'{a * 100 // b}%'


# Не удаляйте код ниже, он нужен для проверки

a = int(input())
b = int(input())
print(get_percent_rounded(a, b))