#словари
words_easy = { 
    "family":"семья", 
    "hand": "рука", 
    "people":"люди", 
    "evening": "вечер",
    "minute":"минута", 
}

words_medium = { 
    "believe":"верить", 
    "feel": "чувствовать", 
    "make":"делать", 
    "open": "открывать",
    "think":"думать", 
}

words_hard = { 
    "rural":"деревенский", 
    "fortune": "удача", 
    "exercise":"упражнение", 
    "suggest": "предлагать",
    "except":"кроме", 
}

levels = {
   0: "Нулевой", 
   1: "Так себе", 
   2: "Можно лучше", 
   3: "Норм", 
   4: "Хорошо", 
   5: "Отлично",
}

answers = {}

right_answers = 0


hards = {
    "легкий":words_easy,
    "средний":words_medium,
     "сложный":words_hard,
     }

#Выбор сложности
hard = input("Выберете уровень сложности: (Легкий, средний, сложный):")

work_dict = hards[hard]

#Запуск цикла

for key, value in work_dict.items():
  answer = input(f"{key}, {len(value)} букв, начинается на {value[0]}... Ответ:")
  if answer == value:
    print(f'Верно, {key.title()} - это {value}')
  else:
    print(f'Неверно. {key.title()} - это {value}')  

answers[key] = answer == value

#счетчик ответов

print()
print('Правильно отвечены слова:')

for word, bool_value in answers.items():
  if bool_value is True:
    print(word)
    right_answers += 1    

print()
print('Неправильно отвеченые слова:')

for word, bool_value in answers.items():
  if bool_value is False:
    print(word)
       
#итог

print(f'Ваш ранг:{levels[right_answers]}')

