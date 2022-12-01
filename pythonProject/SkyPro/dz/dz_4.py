# словари со словами
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
    "except":"кроме", }
levels = {
   0: "Нулевой", 
   1: "Так себе", 
   2: "Можно лучше", 
   3: "Норм", 
   4: "Хорошо", 
   5: "Отлично",
}
answers = {} # ответы

# пользователь выбирает сложность

dict_user = {'легкий' : words_easy, 'средний': words_medium, "сложный": words_hard}

user_input = input('Выберите уровень сложности: легкий / средний / сложный: ')
if user_input in "легкий / средний / сложный":
    print("Начнем!")
else:
    print('Включите программу, когда будете готовы.')
    quit()

words = dict_user[user_input]

# цикл с вопросами

for k,v in words.items():
    user_answer = input(f'Программа: {k}, {len(v)} букв, начинается на {v[0]}: ')
    if user_answer == v:
        print(f'Программа: Верно, {k} — это {v}.')
        answers[k] = True
    else:
        print(f'Программа: Неверно. {k} — это {v}.')
        answers[k] = False

# цикл с ответами
        
rang = 0
for key, val in answers.items():
    if val == True:
        print(f'Правильно отвечены слова: {key}')
        rang += 1
        
for tr, fl in answers.items():
    if fl == False:
        print(f'Неправильно отвечены слова: {tr}')

# ранг пользователя

print(f'Ваш ранг: {levels[rang]}')