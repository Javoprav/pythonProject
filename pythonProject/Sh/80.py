s = 0
for k in range(3,10):
 s = s + 6
 if s == 30:
  break
print(s)

k = 0
for m in range(1,10,2):
 k = k + 6
 if s == 30:
  break
print(k)

s = 10
for k in range(5):
 s -= k
 if s == 30:
  break
print(s)

s = -30
while s < 0:
 s += 6
 if s == -8:
  continue
 if s == -6:
  continue
print(s)

s = 1
n = 15
while n > 0:
 n = n - s
 s = s * 2
 if s == 8:
  continue
 if s == 64:
  continue
print(n)

k = 1
while k <= 64:
 k = k*2
 if k == 8:
  continue
 if k == 63:
  continue
print(k)

s = 10
while k < 5:
 s -= k
print(s)

s = -30
for s in range(-30,-5):
 s += 6
print(s)

s = -30
while s < 0:
 s += 6
print(s)

for i in range(25,30,2):
 print(i)

i = 7
while i > 0:
 i = 2*i-10
print(i)

for i in range(3):
 while i != 0:
  print('Ура!')
  i = i - 1

a = 35
while a <= 50:
 if a == 43 or a == 47:
  continue
 if a % 2 == 1:
  print(a)
 a += 2

a = 'Key'
b = 2021
print(b % 10)
for i in a:
 print(b % 10)
 b = b // 10

