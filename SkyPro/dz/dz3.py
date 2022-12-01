# 2 авриант
# Создание переменных
# 2 авриант
# Создание переменных
questions = ["My name ___  Vova ", "I ___ a coder ", "I live ___ Moscow "]
answers = ["is", "am", "in"]
counter = 0
question = 0
percent = 0

score = 0
# Приветствие
print('Привет! Предлагаю проверить свои знания английского! Наберите "ready", чтобы начать!')
user_answer = input()

# приветствие пользователя
if user_answer == "ready": # проверка пользователя
  for i in range(len(questions)): # основной цикл с вопросами
      life = 3 # перебор попыток
      while life > 0:
          answer = input(questions[i])
          if answer == answers[i]:
           print('Ответ верный! \nВы получаете 10 баллов!')
           counter += 10
           question += 1
           percent += 33.3
           score += life *10
           break
          else:
              life -= 1
              print(f'Осталось попыток: {life}, попробуйте еще раз!')

  percent_question = question / 3 * 100  # статистика

  print('Вот и все!')
  print(f'Вы ответили на {question} вопросов из 3 верно.')
  print(f'Вы заработали {counter} баллов.')
  print(f'Это {round(percent_question)} процентов.')
else:
 print('Кажется, вы не хотите играть. Очень жаль.')

