actions = ['buy it', 'use it', 'break it', 'fix it']

action_indexes = range(len(actions)) # [0, 1, 2, 3]

for act_idx in action_indexes:
   print(actions[act_idx])
    
print('______________________________')

for x in actions:
   print(x)

print('______________________________')

club = ["ЦСКА", "Спартак", "Динамо"]

for i in range(len(club)):
  print(i+1, club[i])

print('______________________________')

for i in range(10, 0, -2) :
    print(i)

print('______________________________')

i = [item for item in range(1,10)]
print(i)

print('______________________________')

numbers = [-2, -1, 0, 1, 2, "1", '2']

numbers_positive = []

for num in numbers:
    if int(num):
        numbers_positive.append(num)

print(numbers_positive)
# Выведет [1, 2]

print('______________________________')

messages_count = int(input())
if messages_count > 0:
  print ("Есть новые сообщения")


s = 'abc' 
t = [10, 20, 30]

# {'a': 10, 'b': 20, 'c': 30}

dict_st = {}
for i in range(3):
    dict_st[s[i]] = t[i]
print(dict_st)

#   print(dict(zip(s,t)))

