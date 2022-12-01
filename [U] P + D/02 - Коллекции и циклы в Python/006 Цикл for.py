number = [1, 2, 3, 4, 5]
for x, item in enumerate(number):
 number[x] += 20
print (number)

nam = "Марадонна"
for x in nam:
 print (x)

for _ in range (1,5):
 print ("Ошибка")

a = ("Alexey", 33, 3.158)
for q in a:
  print(q)

list = [("Васе", 22), ("Жоре", 33), ("Олеху", 44)]
for (name, age) in list:
  print(f'{name} где то {age}, но он точно не помнит')

dict = {
  "Васе": 22, 
  "Жоре": 33,
  "Олеху": 44
}
for f in dict:
  print(f)

dict = {
  "Васе": 22, 
  "Жоре": 33,
  "Олеху": 44
}
for f in dict.items():
  print(f)

print(type(f))

dict = {
  "Васе": 22, 
  "Жоре": 33,
  "Олеху": 44
}
for t, u in dict.items():
  print(f"Ключ \"{t}\" и значение \"{u}\"")

for vallue in dict.values():
  print(vallue)