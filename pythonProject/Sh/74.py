a = input('Введите слово: ')
for i in a:
 if i == 'к':
  print('В этом слове есть буква "к"')

n = 1
while n <= 20:
 print(n)
 n = n + 1

a = 0
while True:
 a = a + 1
 if a == 6:
  break
  print(a)

for a in range(11):
 if a == 5 or a == 8:
  continue
 print(a)

count = 0
for i in range(1,4):
 for j in range(1,5):
  count = count + 1
print(count)