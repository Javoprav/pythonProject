r = 10     # площадь круга
s = 3.1415 * (r ** 2)
print(s)

print('____________________')

def sq_ring(p):
 s = 3.1415 * (p ** 2)
 print(s)

sq_ring(10)

print('____________________')

def sq_ring(p):
 s = 3.1415 * (p ** 2)
 return(s)

p = 10

print(sq_ring(p))

# Вычисление периметра треугольника


def get_square(w,h):
    return 2 * (w + h)

print(get_square(5, 5))

print('____________________')

def print_text(msg, end = '!', sep = ': '):
    print ('Сообщение' + sep + msg + end)

print_text("текст")
print_text("текст", "?")
print_text("текст", "?", " ")
print_text("текст", sep = " ")