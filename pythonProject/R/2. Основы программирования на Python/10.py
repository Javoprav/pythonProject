li = [1, 5, 0, -5, 2.5]
for n in li:
    print(n)

print('-------------------------------------------')

str = 'Python'
print(str[0])
print(str)
for s in str:
    print(s)

for x in str:
 if x == 'b':
  break
else:
    print('Символа "b"  в строке ', str, 'нет')

list2 = range(2,15)
print(list2[2])
for l in list2:
    print(l)
    
print('-------------------------------------------')

a = [i for i in range(1,10)]
print(a)
a = [i*2 for i in range(1,10)]
print(a)
a = [i for i in range(1,10) if i % 2 == 0]
print(a)

ar = [1, 2, 3, 4, 5, 6, 7, 8, 9]
x = 0
y = 0
while y < 9:
    x += 2
    ar[y] = x
    y += 1
print(ar)
