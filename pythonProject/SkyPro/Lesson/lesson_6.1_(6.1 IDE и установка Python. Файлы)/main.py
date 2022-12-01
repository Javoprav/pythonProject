from pin import check_pin
user_input = input("Введите ваш ПИН-код")
check_pin(user_input)
if check_pin(user_input) == True:
 print("Такой ПИН-код подходит")
else:
 print("Такой ПИН-код НЕ подходит")