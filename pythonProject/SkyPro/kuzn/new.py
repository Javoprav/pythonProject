'''### Задача 8

На внешнем сервере хранится список со вложенным словарем. Напишите функцию `load_names(url)`, которая превратит его в список вида:
[”Имя”, “Имя”, “Имя”, ”Имя”]
'''
import requests as requests
import json

URL = "https://jsonkeeper.com/b/NPMT"

def load_names(url):
    req = requests.get(url)
    data = req.json()
    list_names = []  #
    list_names = set()
    for i in data:
        list_names.add(i["first_name"])
        #list_names.append(i["first_name"])  #
    return list(list_names)
    #names = set(i["first_name"] for i in data)
    #return list(names)

print(load_names(URL))