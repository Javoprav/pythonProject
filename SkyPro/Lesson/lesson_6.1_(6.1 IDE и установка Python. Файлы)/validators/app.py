from validators.validate_pin import validate_pin
from validators.validate_card import validate_card


card_number = input("Введите ваш номер карты: ")

card_pin = input("Введите ваш ПИН-код: ")

if validate_pin(card_pin) == True:
 print("Такой ПИН-код подходит")
else:
 print("Такой ПИН-код НЕ подходит")

if validate_card(card_number) == True:
 print("Номер карты допустимый")
else:
 print("Номер карты не допустимый")
