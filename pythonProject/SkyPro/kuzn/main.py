'''### Задача 8
На внешнем сервере хранится список со вложенным словарем.
Напишите функцию `load_names(url)`, которая превратит его в список вида:
[”Имя”, “Имя”, “Имя”, ”Имя”]
URL = "https://jsonkeeper.com/b/NPMT"
'''

import request
import os
os.path.join('data', 'users', 'all.txt')

URL = requests.get("https://jsonkeeper.com/b/NPMT")
data = json.loads(URL.text)
def load_names(url):
    list_names = []
    with open(url, 'r', encoding='utf-8') as f:
        for i in f:
            list_names.append(i["first_name"])
    return list_names

print(URL)

'''[{"id":1,"first_name":"Kipp","last_name":"Loges"},
{"id":2,"first_name":"Farrel","last_name":"Roseaman"},
{"id":3,"first_name":"Toddie","last_name":"Gare"},
{"id":4,"first_name":"Loretta","last_name":"Kienlein"},
{"id":5,"first_name":"Burl","last_name":"Markus"},
{"id":6,"first_name":"Marena","last_name":"Sibbit"},
{"id":7,"first_name":"Herc","last_name":"Ormshaw"},
{"id":8,"first_name":"Dannel","last_name":"Ranscomb"},
{"id":9,"first_name":"Nonnah","last_name":"Keep"},
{"id":10,"first_name":"Ferrel","last_name":"Orrum"}]'''