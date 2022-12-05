def get_word():
    items = random.sample(list_words, 1)
    result = ''.join(items)
    return result