'''Анализатор текста
В этой части программы определяется функция, которая подсчитывает, сколько раз символ встречается в строке.
В качестве аргументов этой функции присвоены текст файла и один символ; функция затем возвращает число упоминаний символа в тексте.
Теперь мы можем использовать ее для нашего файла.'''

def count_char(text, char):
  count = 0
  for c in text:
    if c == char:
      count += 1
  return count

filename = input("Enter a filename: ")
with open(filename) as f:
  text = f.read()
print(count_char(text, "r"))

'''Следующая часть программы находит какой процент текста приходится на каждый из символов алфавита. '''

def count_char(text, char):
    count = 0
    for c in text:
        if c == char:
            count += 1
    return count

file = open("newfile.txt", "w")
file.write("""Ornhgvshy vf orggre guna htyl.
Rkcyvpvg vf orggre guna vzcyvpvg.
Fvzcyr vf orggre guna pbzcyvpngrq.
Syng vf orggre guna arfgrq.
Fcenfr fv orggre guna qrafr.
Ernqnovyvgl pbhagf.
Fcrpvny pnfrf nera'g fcrpvny rabthu gb oernx gur ehyrf.
Nygubhtu cenpgvpnyvgl orgnf chevgl.
Reebef fubhyq arire cnff fvyragyl.
Hayrff rkcyvpvgyl fvyraprq.
Va gur snpr bs nzovthvgl, ershfr gur grzcgngvba bg thrff.
Gurer fubhyq or bar-- naq cersrenoylbayl bar --boivbhf jnl gb qb vg.
Nygubhtu gung jnl znl abg or boivbhf ng svefg hayrff lbh'er Qhgpu.
Abj vf orggre guna arrire.
Nygubhtu arire vf bsgra orggre guna *evtug* abj.
Vs gur vzcyrzragngvba vf uneq gb rkcynva, vg'f n onq vqrn.
Vs gur vzcyrzragngvba vf rnfl gb rkcynva, vg znl or n tbbq vqrn.
Anzrfcnprf ner bar ubaxvat terng vqrn -- yrg'f qb zber bs gubfr!""")
file.close()
filename = "newfile.txt"
with open(filename) as f:
    text = f.read()

for char in "abcdefghijklmnopqrstuvwxyz":
    perc = 100 * count_char(text, char) / len(text)
    print("{0} - {1}%".format(char, round(perc, 2)))

####### Удаление знаков из строки

def remove_from_string(string, *symbols_to_remove):

  for symbol in symbols_to_remove:
    string = string.replace(symbol,"")
  return string

remove_from_string("О! Смотри, можно удалить все знаки препинания сразу?", "?", "!", ",", ".", "–")

####### Считывание документации

def remove_from_string(string, *symbols_to_remove):
  """Удаляет символы, перечисленные после первого аргумента  """

  for symbol in symbols_to_remove:
    string = string.replace(symbol,"")
  return string

print(remove_from_string.__doc__) # Считывание документации


####### проверяет картавость слова

def has_rrr(word):
  word = word.lower()
  if "р" in word:
    return True
  else:
    return False
# Не удаляйте код ниже, он нужен для проверки
word = input()
result = has_rrr(word)
print(result)


########## принимает целое число от 2 до 5 и возвращает оценку

grades = {2:"Плохо", 3:"Удовлетворительно", 4:"Хорошо", 5:"Отлично"}

def get_grade(grade):
    return grades[grade]
# Не удаляйте код ниже, он нужен для вызова функции и проверки
grade = int(input())
print(get_grade(grade))


########### принимает количество баллов и возвращает оценку

def get_grade(points):
  if points >= 0 and points <= 40:
    return 'Плохо'
  elif points > 40 and points <= 60:
    return 'Удовлетворительно'
  elif points > 60 and points <= 80:
    return 'Хорошо'
  elif points > 80 and points <= 100:
    return 'Отлично'

   # return points
# Не удаляйте код ниже, он нужен для проверки

points = int(input())
grade = get_grade(points)
print(grade)


############## принимает час и возвращает время суток

def get_period(hour):
  if hour >= 0 and hour <= 6:
    return "ночь"
  elif hour > 6 and hour <= 11:
    return "утро"
  elif hour > 12 and hour <= 17:
    return "день"
  elif hour > 18 and hour <= 24:
    return 'вечер'
# Не удаляйте код ниже, он нужен для проверки

hour = int(input())
time_of_day = get_period(hour)
print(time_of_day)


########## принимает время в секундах, возвращает словарь в формате:
########## {"min": мин, "sec": сек}

def get_min_sec(sec):
  min_sec = {}
  min_sec['min'] = sec // 60
  min_sec['sec'] = sec % 60
  return min_sec
 # return print(f'"min": {min}, "sec": {s}')

# Не удаляйте код ниже, он нужен для проверки

value = int(input())
result = get_min_sec(value)  
print(result)


######## Расчет процентов

def get_percent_rounded(a, b):
  
  return f'{a * 100 // b}%'

# Не удаляйте код ниже, он нужен для проверки

a = int(input())
b = int(input())
print(get_percent_rounded(a, b))


#############  хештеги одним списком

def get_hashtags(text):
    words = text.split(" ")
    hashtags = []
    for word in words:
        if word[0] == '#':
          hashtags.append(word[1:])
        else:
            pass
    return hashtags
# Не удаляйте код ниже, он нужен для проверки    
words = input()
result = get_hashtags(words)
print(result)


'''Площадь круга
Формула вычисления площади'''

import math
def get_square(radius):
  r = radius ** 2 * round(math.pi,2)
  return r
 #### # r = radius ** 2 * 3.14
  ##### return r
# Не удаляйте код ниже, он нужен для проверки

radius = int(input())
square = get_square(radius)
print(square)


'''Самое длинное слово'''

def get_longest(words):
  longest_word = ''
  for i in words:
    if i > longest_word:
      longest_word = i 
  return longest_word
    
# Не удаляйте код ниже, он нужен для проверки
word = input().split(" ")
result = get_longest(word)
print(result)
get_longest(["еж" , "мышь", "стриж"]) # Вернет "стриж"
get_longest(["aaa", "aa", "a"]) # Вернет "aaa"
get_longest(["——-", "—-", "-"]) # Вернет "——-"
get_longest(["a", "a", "a"]) # Вернет "a"


