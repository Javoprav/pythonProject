x = 'Alex'
print(x)
y = 'text 123'
print(y)
# z = 'some 'long' text' # ошибка в одинаковых ковычках
c = 'some "long" text'
print(c)
z = 'some \'long\' text'
print(z)
v = r'C:\Users\dell\desktop' # r или // для определения слэша как текста
print(v)
b = "текст с новой строки \nтекст с новой строки \nтекст с новой строки" # \n
print(b)
text = str('hello world')
print(text)
print(text[0])
print(text[0]+text[1])
print(text[0]+text[6])
print(text[-1]+text[6])
print(text[6:]+text[6])
print(text[6:]+" "+text[:6])
print(text[6:8])
print(text[::1])
print(text[::2])
print(text+' '+text)
print(text*3)