import os
import json
profi = os.path.join('data', 'professions.json')

def load_professions(prof):
    with open(profi, 'r', encoding='utf-8') as f:
        data = json.load(f)
        for i in data:
            if i["title"].lower() == prof.lower():
                fitness = i["skills"]
                #student = i["full_name"]
                #skl = i["skills"]
    return f'{fitness}'

us_inp = input()
print(load_professions(us_inp))