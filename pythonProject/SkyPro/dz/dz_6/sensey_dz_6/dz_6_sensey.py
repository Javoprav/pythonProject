'''# Урок  6. Локальный Python и фaйлы. Домашнее задание

Привет, это Артем из Mail.ru!

![Untitled (6).png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/55afcd3d-74ce-4410-b990-ff79450d1d76/Untitled_(6).png)

На этой неделе мы начали работать с Python локально и разбираться с файлами. В домашнем задании мы применим все эти новые навыки!

На первом курсе мы разрабатываем разные консольные  (не имеющие интерфейса) приложения для обучения английскому.  Еще одно полезное упражнение — это составление слов из букв. Мы будем перемешивать буквы в словах, а пользователь — их отгадывать!

**Шаг 1.** Создайте файл `words.txt`, где будут храниться английские слова. Например, такой:

```python
python
squirrel
flask
cucumbers
```

**Шаг 2.** В начале работы программа просит пользователя представиться и запоминает его имя.

```python
Программа: Введите ваше имя
Пользователь: Василий
```

**Шаг 3.** После этого программа выбирает первое слово из списка, перемешивает буквы и предлагает пользователю его отгадать.

```python
Программа: ****Угадайте слово: ontyph
Пользователь: python
Программа: Верно! Вы получаете 10 очков.
```

```python
Программа: ****Угадайте слово: ontyph
Пользователь: java
Программа: Неверно! Верный ответ – python.
```

**Шаг 4.** Когда слова закончились, программа заносит рекорд пользователя в файл `history.txt` с историей. Например:

```python
Игорь  200
Алексей  180
Василий  120
Игорь  200
Алексей  180
Василий  120
Игорь  200
Алексей  180
Василий  120
```

**Шаг 5.** В конце необходимо вывести статистику из прошлых игр, с учетом этой игры.

```python
Всего игр сыграно: 27
Максимальный рекорд: 200
```

В программе с помощью функций должны быть сделаны:

- чтение слов из файла,
- чтение топа игроков,
- запись в топ игроков.

Критерии проверки:

- [ ]  Использованы верные режимы чтения для файлов.
- [ ]  Файлы закрываются после работы.
- [ ]  Корректная работа с переносами строк.
- [ ]  Чтение и запись выполняются в функциях с корректными аргументами и операторами return.

Демонстрируемый навык:

- [ ]  Чтение файлов.'''

from utils import load_words, change_word, write_history, read_history

words_txt = 'words.txt'
history_txt = 'history.txt'
print("Введите имя: ")
user_name = input()
words = load_words(words_txt)
score = 0
for word in words:
    print(change_word(word))
    user_answer = input()
    if user_answer.lower().strip(' ') == word:
        print('Верно! Вы получаете 10 очков.')
        score += 10
    else:
        print(f'Неверно! Верный ответ – {word}.')
write_history(history_txt, user_name, score)
print(read_history(history_txt))



############################### main_7.py
import random

def load_words(filename):

    new_lines = []
    with open(filename, 'r', encoding='utf-8') as f:
        for line in f.readlines():
            new_lines.append(line.strip('\n'))
    return new_lines

def change_word(word):
    word = list(word)
    random.shuffle(word)
    return ''.join(word)

def write_history(filename, user_name, score):
    with open(filename, 'a', encoding='utf-8') as f:
        f.write(f'{user_name} {score}\n')

def read_history(filename):
    max = 0
    count = 0
    
    with open(filename, 'r', encoding='utf-8') as f:
        for line in f.readlines():
            count += 1
            score = int(line.split(' ')[1])
            if score > max:
                max = score
    return f'Всего игр сыграно: {count}\nМаксимальный рекорд: {max}'