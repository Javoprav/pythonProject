employees = {
"...": {"f": "" , "i": "", "o": "", "pass": "", "birthday": "" ,"phone": "", "position": ""},
}

sotr_1 = 'Киселёв / Всеволод / Эдуардович / 342 020 / 14 ноября 2001 года / +7 (908) 161-64-28 / главный инженер'
sotr_2 = 'Довлатова / Эмилия /  Ефимовна / 342 000 / 18 мая 2001 года / +7 (924) 588-50-15 / технолог'
sotr_3 = 'Аверин / Мартын / Егорович / 217 340 / 12 февраля 1981 года / +7 (933) 768-22-15 / технолог'
sotr_4 = 'Князева / Августа / Егоровна / 320 021 / 2 июля 1984 года / +7 (965) 886-27-01 / расфасовщик'
sotr_5 = 'Шанская / Аграфена / Семёновна / 116 404 / 7 июля 1982 года/ +7 (954) 940-47-96 / психолог для рыб'

sotr_1 = sotr_1.replace(' ', '').replace('/', ',').split(',')
sotr_2 = sotr_2.replace(' ', '').replace('/', ',').split(',')
sotr_3 = sotr_3.replace(' ', '').replace('/', ',').split(',')
sotr_4 = sotr_4.replace(' ', '').replace('/', ',').split(',')
sotr_5 = sotr_5.replace(' ', '').replace('/', ',').split(',')
print(sotr_5)

sotr = [sotr_1, sotr_2, sotr_3, sotr_4, sotr_5]

'''for k,v in employees.items():
    employees[sotr[0]] = sotr

print(employees)

for employee in employees.values():
  for key, value in employee.items():
      print(key, value)
  print("-")'''