def validate_pin(pin):
    """ Проверяет, является ли ПИН-код последовательностью 4 цифр """
    if not pin.isdigit():
      return False
    if len(pin) != 4:
      return False
    return True