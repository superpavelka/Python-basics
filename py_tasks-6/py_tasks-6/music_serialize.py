import pickle
import json

my_favourite_group = {
'name': 'Г.М.О.',
'tracks': ['Последний месяц осени', 'Шапито'],
'Albums': [{'name': 'Делать панк-рок','year': 2016},
{'name': 'Шапито','year': 2014}]}


mfg_b = pickle.dumps(my_favourite_group)
print(type(mfg_b))
print(mfg_b)

mfg_json = json.dumps(my_favourite_group)
print(type(mfg_json))
print(mfg_json)

with open('group.pickle','wb') as f_b:
    pickle.dump(my_favourite_group, f_b)

with open('group.json', 'w', encoding = 'utf-8') as f_json:
    json.dump(my_favourite_group, f_json)
