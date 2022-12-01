items_count = 0
items_sum = 0
row_index = 0

with open('purchases.txt') as file:
    for item in file:
        row_index += 1    # индекс который ищет ошибку
        if item.count(' ') > 2:
            print(f'В строке {row_index} есть ошибка') #  определение не правильной строки
            continue
        item, quant, prise = item.strip().split(' ')
        items_count += 1
        items_sum += int(prise) * int(quant)

print(f'В списке {items_count} позиций. Сумма {items_sum} Р.')
print("� �����")

print("� �����")
