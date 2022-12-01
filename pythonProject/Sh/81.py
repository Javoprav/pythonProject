count = 0
i = 0
j = 0
while i <= 4 and j <= 3:
 count = count + 1 * 3
 j = j + 1
 i = i + 1
print(count)

i = 0
while i <= 9:
 i += 1
 if i%2 == 0:
  print(i,"- четное")
 else:
  print(i,"- нечетное") # B

a = 0
for a in range(5):
 print(a)      #  A

for i in range(3):
 a = int(input("Введите число")) # D
 print(a*5)

