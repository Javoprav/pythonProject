vals = [1, 2, 3, 4, 5, 6, 7, 8, 9]
summa = 0
for x in vals:
    if x % 2 == 0:
        continue
    else:
        summa += x
    if summa > 10:
        break
print(summa)