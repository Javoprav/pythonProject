'''# Кузница по курсовой 2
### Классы
**Задача 1**
Создайте класс Player, у которого есть name и score (по умолчанию = 0).
Напишите методы `score_up() и score_down()`, которые увеличивают и уменьшают score на 1.  Не забудьте про repr!'''


class Player:
    def __init__(self, name, score=0):
        self.name = name
        self.score = score

    def score_up(self):
        self.score += 1

    def score_down(self):
        self.score -= 1

    def __repr__(self):
        return f'Player {self.name, self.score}'


pl = Player('Jack', 15)
pl.score_up()
pl.score_up()
pl.score_up()
pl.score_up()
pl.score_down()

print(pl)

'''Задача 2
Создайте класс WordStorage – у него есть одно поле - words, список строк,  изначально пустое. У него должно быть 3 метода:
add_word(word) добавляет слово
remove_word(word) удаляет слово
fetch_words() возврашает 
Не забудьте про repr!'''


class WordStorage:
    def __init__(self, words=[]):
        self.words = words

    def add_word(self, word):
        self.words.append(word)

    def remove_word(self, word):
        self.words.remove(word)

    def fetch_words(self):
        return self.words

    def __repr__(self):
        return f'WordStorage {self.words}'


wor = WordStorage()
wor.add_word(15)
wor.add_word(20)
wor.add_word(30)
print(wor)

'''Задача 3
Создайте класс Word. У него есть одно поле – value. Добавьте методы: get_value() - возвращает значение , set_value(new_value) - задает новое слово, get_letters() –  метод возвращает уникальный сет букв текущего слова. has_letter(letter) – возвращает есть ли переданная буква в текущем слове. – Не забудьте про repr!'''

'''Задача 3
Создайте класс Word. У него есть одно поле – value. Добавьте методы: get_value() - возвращает значение , set_value(new_value) - задает новое слово, get_letters() –  метод возвращает уникальный сет букв текущего слова. has_letter(letter) – возвращает есть ли переданная буква в текущем слове. – Не забудьте про repr!'''


class Word:
    def __init__(self, value):
        self.value = value

    def get_value(self):
        return self.value

    def set_value(self, new_value):
        self.value = new_value

    def get_letters(self):
        set_value = set(self.value)
        return set_value

    def has_letter(self, letter):
        return letter in self.value

    def __repr__(self):
        return f'Word {self.value}'


word = Word('word')

print(word)
print(word.get_value())
word.set_value('Leo Messi')
print(word)
print(word.get_letters())
print(word.has_letter('s'))

'''### Функции загрузки
**Задача 1**
Создайте класс `Word` c полем value и без методов
Заведите файл words.txt со словами:
```python
owl
cat
dog
```
Напишите функцию `load_words`(), которая загрузит слова и вернет три экземпляра в списке words. Не забудьте про repr'''
import os

file = os.path.join('words.txt')


class Word:
    def __init__(self, value):
        self.value = value

    def load_words(self):
        list = []
        with open(file, 'r', encoding='utf-8') as f:
            for i in f:
                list.append(i.rstrip())
        return list

    def __repr__(self):
        return f'Word {self.value}'


word = Word('Onopko')
print(word)
print(word.load_words())

'''**Задача 2**
Создайте класс BasicWord c полями word , subwords.  Создайте файл `data.json` :
```python
{"word": "питон", "subwords": ["тип", "топ", "тон"]}
```
Напишите функцию, которая загрузит данные из файла и создаст на его основе экземпляр класса BasicWord.'''
import os
import json


class BasicWord:
    def __init__(self, word='', subwords=''):
        self.word = word
        self.subwords = subwords

    def set_words(self):
        file = os.path.join('data.json')
        with open(file, 'r', encoding='utf-8') as f:
            data = json.load(f)
            self.word = data["word"]
            self.subwords = data["subwords"]

    def __repr__(self):
        return f'BasicWord {self.word, self.subwords}'


q1 = BasicWord('kuku', 'ruku')
print(q1)
q1.set_words()
print(q1)

'''**Задача 3**
Создайте класс `WordManager` c полем words.
У класса должен быть один метод `get_random_word()`, который возвращает случайное слово из поля `words`
 Создайте файл `data.json`.
```python
["cat","dog","owl","mouse","fox"]
```
Создайте функцию `create_data_manager_from_json(path)` которая загрузит данные из файла и создаст на их основе экземпляр класса  `WordManager`.'''

import random
import os
import json

file = os.path.join('data.json')


class WordManager:
    def __init__(self, words):
        self.words = words

    def get_random_word(self, words):
        return random.choice(words)

    def __repr__(self):
        return f'WordManager {self.words}'


def create_data_manager_from_json(path):
    with open(path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    return data


list_words = create_data_manager_from_json(file)
wordm = WordManager('питоня')
print(wordm)
print(wordm.get_random_word(list_words))