'''### Задача 1

Напишите функцию `get_unique_names(names)`, которая принимает список и возвращает уникальные элементы из него в виде списка.'''

def get_unique_names(names):
    names_set = set(names)
    return names_set

names = ["Yvor", "Wendell", "Hogan", "Sadella", "Yvor", "Sadella", "Hogan"]

unique_names = get_unique_names(names)

print(unique_names)

### Задача 2

'''Напишите функцию, которая печатает имена из списка словарей в таком формате:

Kingsley
Tobit
Pace
Andreas
Anthia
'''

users = [{
  "id": 1,
  "first_name": "Kingsley",
  "url": "https://weather.com/aliquet/at/feugiat/non/pretium.jsp"
}, {
  "id": 2,
  "first_name": "Tobit",
  "url": "http://pen.io/sapien/cursus/vestibulum/proin/eu/mi/nulla.json"
}, {
  "id": 3,
  "first_name": "Pace",
  "url": "http://ucsd.edu/justo/morbi/ut/odio/cras/mi.json"
}, {
  "id": 4,
  "first_name": "Andreas",
  "url": "https://ifeng.com/morbi/vestibulum/velit.png"
}, {
  "id": 5,
  "first_name": "Anthia",
  "url": "https://google.com/eu/orci.aspx"
}]

def get_names_from_user_list(names):
    list = []
    for name in names:
        list.append(name["first_name"])
    return [print(n) for n in list]

print(get_names_from_user_list(users))

'''### Задача 2.5
Напишите функцию `get_ids(users)`, которая возвращает id из списка словарей в таком формате:
[1,2,3,...]
# Вернет [1,2,3,4,5]
'''
users = [{
  "id": 1,
  "first_name": "Kingsley",
  "url": "https://weather.com/aliquet/at/feugiat/non/pretium.jsp"
}, {
  "id": 2,
  "first_name": "Tobit",
  "url": "http://pen.io/sapien/cursus/vestibulum/proin/eu/mi/nulla.json"
}, {
  "id": 3,
  "first_name": "Pace",
  "url": "http://ucsd.edu/justo/morbi/ut/odio/cras/mi.json"
}, {
  "id": 4,
  "first_name": "Andreas",
  "url": "https://ifeng.com/morbi/vestibulum/velit.png"
}, {
  "id": 5,
  "first_name": "Anthia",
  "url": "https://google.com/eu/orci.aspx"
}]

def get_ids(users):
    list = []
    for name in names:
        list.append(name["id"])
    return list

print(get_ids(users))

'''### Задача 3
Напишите функцию `filter_yellow_only(animals)`, которая выводит только тех животных, которые желтые (yellow)
Пример вывода:
Francolinus coqui is Yellow
Petaurus norfolcensis is Yellow'''

animals = [{
  "id": 1,
  "specie": "Francolinus coqui",
  "color": "Yellow"
}, {
  "id": 2,
  "specie": "Petaurus norfolcensis",
  "color": "Yellow"
}, {
  "id": 3,
  "specie": "Pseudoleistes virescens",
  "color": "Teal"
}, {
  "id": 4,
  "specie": "Sula dactylatra",
  "color": "Maroon"
}, {
  "id": 5,
  "specie": "Echimys chrysurus",
  "color": "Teal"
}]

def filter_yellow_only(animals):
    yellow_cat = {}
    for line in animals:
        if line["color"] == "Yellow":
            yellow_cat[line["specie"]] = "Yellow"
    return yellow_cat

yellow_only = filter_yellow_only(animals)


'''### Задача 4
Напишите функцию  `filter_violet_only(animals)`, которая возвращает в формате списка id только тех животных, которые фиолетовые (`violet`) 
Пример ввода:'''

animals = [{
  "id": 1,
  "specie": "Eumetopias jubatus",
  "color": "Violet"
}, {
  "id": 2,
  "specie": "Tayassu tajacu",
  "color": "Violet"
}, {
  "id": 3,
  "specie": "Ephipplorhynchus senegalensis",
  "color": "Teal"
}, {
  "id": 4,
  "specie": "Pycnonotus barbatus",
  "color": "Indigo"
}, {
  "id": 5,
  "specie": "Acridotheres tristis",
  "color": "Violet"
}, {
  "id": 6,
  "specie": "Hippotragus niger",
  "color": "Teal"
}, {
  "id": 7,
  "specie": "Redunca redunca",
  "color": "Turquoise"
}]

def filter_violet_only(animals):
    violet_list = []
    for i in animals:
        if i["color"] == "Violet":
            violet_list.append(i["id"])
    return violet_list

# Вернет [1, 2, 5]
print(filter_violet_only(animals))

'''### Задача 5
Напишите функцию  `filter_violet_only(animals)`, которая возвращает в формате списка **словари** только тех животных, которые фиолетовые (`violet`)
# Должна вернуть 
[{
  "id": 1,
  "specie": "Eumetopias jubatus",
  "color": "Violet"
}, {
  "id": 2,
  "specie": "Tayassu tajacu",
  "color": "Violet"
}, {
  "id": 5,
  "specie": "Acridotheres tristis",
  "color": "Violet"
}]
'''

animals = [{
  "id": 1,
  "specie": "Eumetopias jubatus",
  "color": "Violet"
}, {
  "id": 2,
  "specie": "Tayassu tajacu",
  "color": "Violet"
}, {
  "id": 3,
  "specie": "Ephipplorhynchus senegalensis",
  "color": "Teal"
}, {
  "id": 4,
  "specie": "Pycnonotus barbatus",
  "color": "Indigo"
}, {
  "id": 5,
  "specie": "Acridotheres tristis",
  "color": "Violet"
}, {
  "id": 6,
  "specie": "Hippotragus niger",
  "color": "Teal"
}, {
  "id": 7,
  "specie": "Redunca redunca",
  "color": "Turquoise"
}]

def filter_violet_only(animals):
    violet_only = []
    for i in animals:
        if i["color"] == "Violet":
            violet_only.append(i)

    return violet_only

print(filter_violet_only(animals))

'''### Задача 6
Напишите функцию  `get_names_sorted(animals)`, которая возвращает в формате списка строк **названия** всех животных отсортированных по алфавиту.
# Должна вернуть  
["Cygnus atratus", "Macaca fuscata", "Ursus arctos"]'''

animals = [{
  "specie": "Macaca fuscata",
  "color": "Khaki"
}, {
  "specie": "Cygnus atratus",
  "color": "Aquamarine"
}, {
  "specie": "Ursus arctos",
  "color": "Yellow"
}]

def get_names_sorted(animals):
    list = []
    for i in animals:
        list.append(i["specie"])
    list.sort()
    return list

'''my_languages.sort(reverse=True)
sort()'''
print(get_names_sorted(animals))

'''### Задача 7
Напишите функцию  `get_comments_by_post_id(comments, post_id)` которая возврашает только те комментарии, которые к определенному посту.
# Пример вызова get_comments_by_post_id(comments, 1)
 [{
  "author": "Silvio",
  "time": "2:45 PM",
  "comment": "Nullam sit amet turpis elementum ligula vehicula consequat. Morbi a ipsum. Integer a nibh.",
  "post_id": 1
},{
  "author": "Mariellen",
  "time": "6:51 AM",
  "comment": "Nullam porttitor lacus at turpis. Donec posuere metus vitae ipsum. Aliquam non mauris.",
  "post_id": 1
}]'''

comments = [{
  "author": "Werner",
  "time": "2:14 PM",
  "comment": "Integer ac leo. Pellentesque ultrices mattis odio. Donec vitae nisi.",
  "post_id": 3
}, {
  "author": "Raymond",
  "time": "12:48 PM",
  "comment": "Praesent blandit. Nam nulla. Integer pede justo, lacinia eget, tincidunt eget, tempus vel, pede.",
  "post_id": 5
}, {
  "author": "Silvio",
  "time": "2:45 PM",
  "comment": "Nullam sit amet turpis elementum ligula vehicula consequat. Morbi a ipsum. Integer a nibh.",
  "post_id": 1
}, {
  "author": "Shelbi",
  "time": "1:29 AM",
  "comment": "Quisque id justo sit amet sapien dignissim vestibulum. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia Curae; Nulla dapibus dolor vel est. Donec odio justo, sollicitudin ut, suscipit a, feugiat et, eros.",
  "post_id": 5
}, {
  "author": "Barnabas",
  "time": "2:28 PM",
  "comment": "Phasellus sit amet erat. Nulla tempus. Vivamus in felis eu sapien cursus vestibulum.",
  "post_id": 5
}, {
  "author": "Mariellen",
  "time": "6:51 AM",
  "comment": "Nullam porttitor lacus at turpis. Donec posuere metus vitae ipsum. Aliquam non mauris.",
  "post_id": 1
}, {
  "author": "Brandon",
  "time": "1:29 AM",
  "comment": "Sed sagittis. Nam congue, risus semper porta volutpat, quam pede lobortis ligula, sit amet eleifend pede libero quis orci. Nullam molestie nibh in lectus.",
  "post_id": 2
}]


def get_comments_by_post_id(comments, post_id):
    comments_by_post_id = []
    for i in comments:
        if post_id == i["post_id"]:
            comments_by_post_id.append(i)
    return comments_by_post_id

print(get_comments_by_post_id(comments, 1))

