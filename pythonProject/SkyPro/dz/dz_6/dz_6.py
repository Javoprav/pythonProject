'''импорт модулей и создание переменных'''
import random

ball = 0

'''функция чтения из файла со словами'''


def correct_word():
    list_correct_word = []
    file_name = 'words.txt'
    with open(file_name, "r", encoding="utf-8") as file:
        for line in file.readlines():
            list_correct_word.append(line.replace('\n', ''))
    items = random.sample(list_correct_word, 1)
    items_str = ''.join(items)
    return items_str


"""функция шифровки слова"""


def shuffling_letters(word):
    word_as_list = list(word)
    random.shuffle(word_as_list)
    word_ = " ".join(word_as_list).replace(' ', '')
    return word_


"""запись статистики в файл"""


def write_stat():
    with open('history.txt', 'a', encoding="utf-8") as file_w:
        file_w.write(f"{user_name} {ball}\n")


'''вывод статистики'''


def total_g():
    total_games = 0
    max_score = 0
    with open('history.txt', 'r', encoding="utf-8") as file_wr:
        all_games = file_wr.readlines()
        total_games = len(all_games)
        for line in all_games:
            score = int(line.split(" ")[1])  ######## берет 2 слово из строки
            if score > max_score:
                max_score = score
    return f'Всего игр сыграно: {total_games} \nМаксимальный рекорд: {max_score}'


user_name = input('Введите ваше имя: ')

"""основной цикл игры"""
game_cycle = 0
while game_cycle < 4:
    ans_1 = correct_word()
    question_1 = shuffling_letters(ans_1).replace('\n', '')
    print(f'Угадайте слово: {question_1}')
    user_input_1 = input().lower()
    if user_input_1 == ans_1:
        print('Верно! Вы получаете 10 очков.')
        game_cycle += 1
        ball += 10
    else:
        print(f'Неверно! Верный ответ – {ans_1}.')
        game_cycle += 1
        ball -= 10

write_stat()
print(total_g())