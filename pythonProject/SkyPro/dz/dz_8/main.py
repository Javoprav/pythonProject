'''импорты'''

from utils import Question, dict_by, print_stat
import random

'''Основной блок'''

def main():
    dict_question = dict_by()
    print('Игра начинается!')
    question_number = 0
    points_game = 0
    while question_number < 5:
        for i in dict_question:
            quest = Question(i['q'], int(i['d']), i['a'])
            print(f'Вопрос: {quest.build_question()}\nСложность {quest.difficulty}')
            user_answer_input = input()
            quest.user_answer = user_answer_input.lower()
            if quest.is_correct():
                points_game += int(quest.difficulty) * 10
                print(quest.build_positive_feedback())
            else:
                points_game -= int(quest.difficulty) * 10
                print(quest.build_negative_feedback())
            question_number += 1
            print(quest.difficulty)
    quest.points = points_game
    print(print_stat(question_number, quest.points))

main()