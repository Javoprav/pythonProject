'''Проверяет, является ли номер карты 4 группами цифр через пробелы'''
def validate_card(card_number):
    card_segments = card_number.split(" ")
    if len(card_segments) != 4:
        return False
    for segment in card_segments:
        if len(segment) != 4:
            return False
        if not segment.isdigit():
            return False
    return True