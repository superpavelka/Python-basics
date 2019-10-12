import pickle
import json

try:
    with open('group.pickle', 'rb') as f_b:
        my_favourite_group_b = pickle.load(f_b)

    print(my_favourite_group_b)

    with open('group.json', 'r', encoding = 'utf-8') as f_json:
        my_favourite_group_json = json.load(f_json)

    print(my_favourite_group_json)
except FileNotFoundError:
    print('Ошибка! Файлы не найдены!')