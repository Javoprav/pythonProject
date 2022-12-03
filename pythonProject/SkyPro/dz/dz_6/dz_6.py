#import os
import random

list_correct_word = []

file_name = 'words.txt'
with open(file_name, "r") as file:
    for line in file.readlines():
        list_correct_word.append(line.replace('\n', ''))
# print(list_correct_word)

def get_word():
    items = random.sample(list_correct_word, 1)
    result = ''.join(items)
    return result

'''def correct_word():
    file_name = 'words.txt'
    with open(file_name, "r") as file:
     for line in file.readlines():
        correct_word = "".join(line)
        return correct_word.lower()'''
'''def shuffling_letters(word):
    filename = 'words.txt'
    with open(filename, "r") as file_2:
     for line in file_2.readlines():
        word_as_list = list(line)
        random.shuffle(word_as_list)
        word_ = " ".join(word_as_list).replace(' ', '')
        return word_'''
def shuffling_letters(word):
    word_as_list = list(word)
    random.shuffle(word_as_list)
    word_ = " ".join(word_as_list).replace(' ', '')
    return word_

user_name = input('Введите ваше имя: ')

game_cycle = 0
while game_cycle < 4:
    ans_1 = get_word()
    question_1 = shuffling_letters(ans_1).replace('\n', '')
    print(f'Угадайте слово: {question_1}')
    print(ans_1)  ########################
    user_input_1 = input().lower()
    if user_input_1 == ans_1:
        print('Верно! Вы получаете 10 очков.')
        # answers.append(True)
        game_cycle += 1
    else:
        print(f'Неверно! Верный ответ – {ans_1}.')
        # answers.append(False)
        game_cycle += 1


'''game_cycle = 0
while game_cycle < 4:
    ans_1 = correct_word().replace('\n', '')
    question_1 = shuffling_letters(ans_1).replace('\n', '')
    print(f'Угадайте слово: {question_1}')
    print(ans_1)  ########################
    user_input_1 = input().lower()
    if user_input_1 == ans_1:
        print('Верно! Вы получаете 10 очков.')
        # answers.append(True)
        game_cycle += 1
    else:
        print(f'Неверно! Верный ответ – {ans_1}.')
        # answers.append(False)
        game_cycle += 1'''

# print(f'Угадайте слово: {shuffling_letters()}')

'''def read_top_players(name_file):
    max_score = 0

    with open(name_file, 'r', encoding="utf-8") as file:
        total_games = len(file.readlines())
        for line in file.readlines():
            score = int(line.split(" ")[1])
            if score > max_score:
                max_score = score

    return f"Всего игр сыграно: {total_games}\n" \
           f"Максимальный рекорд: {max_score}"'''