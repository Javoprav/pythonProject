from utils import load_words, change_word

if __name__ == '__main__':
    print('Введите ваше имя: ')
    #user_name = input()
    words = load_words('words.txt')
    score = 0
    for word in words:
        print(change_word(word))
        user_answer = input()
        if user_answer.lower().strip(' ') == word:
            print('Верно! Вы получаете 10 очков.')
            score += 10
        else:
            print(f'Неверно! Верный ответ – {word}.')