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