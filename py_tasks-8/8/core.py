import os
import shutil
import datetime


def create_file(name, text=None):
    with open(name, 'w', encoding='utf-8') as f:
        if text:
            f.write(text)
        save_info(f'Было выполнено создание файла {name}')


def create_folder(name):
    try:
        os.mkdir(name)
        save_info(f'Было выполнено создание папки {name}')
    except FileExistsError:
        print('Такая папка уже есть')
        save_info('Ошибка создания папки!')


def get_list(folders_only=False):
    result = os.listdir()
    if folders_only:
        result = [f for f in result if os.path.isdir(f)]
    print(result)


def delete_file(name):
    if os.path.isdir(name):
        try:
            os.rmdir(name)
            save_info(f'Было выполнено удаление папки {name}')
        except FileNotFoundError:
            print('Такой папки не существует!')
            save_info('Попытка удалить несуществующую папку!')
        except OSError:
            print('Папка содержит файлы. Вы уверены что хотите ее удалить? y - да, n - нет')
            choice = input('Ваш выбор:')
            if choice == 'y':
                shutil.rmtree(name)
                print(f'Папка {name} была удалена!')
                save_info(f'Было выполнено удаление папки {name}')
            elif choice == 'n':
                print('Папка не была удалена!')
            else:
                print('Ошибка ввода!')
    else:
        try:
            os.remove(name)
            save_info(f'Было выполнено удаление файла {name}')
        except FileNotFoundError:
            print('Такого файла не существует!')
            save_info('Попытка удалить несуществующий файл!')


def copy_file(name, new_name):
    if os.path.isdir(name):
        try:
            shutil.copytree(name, new_name)
            save_info(f'Было выполнено копирование файла {name}. Новое имя файла {new_name}')
        except FileExistsError:
            print('Такая папка уже есть!')
            save_info('Ошибка копирования папки!')
        except FileNotFoundError:
            print('Такой папки не существует!')
            save_info('Ошибка копирования папки!')
    else:
        try:
            shutil.copy(name, new_name)
            save_info(f'Было выполнено копирование папки {name}. Новое имя папки {new_name}')
        except FileExistsError:
            print('Такой файл уже есть!')
            save_info('Ошибка копирования файла!')
        except FileNotFoundError:
            print('Такого файла не существует!')
            save_info('Ошибка копирования файла!')


def save_info(message):
    current_time = datetime.datetime.now()
    result = f'{current_time} - {message}'
    with open('log.txt', 'a', encoding='utf-8') as f:
        f.write(result + '\n')


def change_folder(name):
    try:
        # меняем рабочую папку во время выполнения скрипта, чтобы лог файл писался в рабочую папку
        os.chdir(os.getcwd() + '\\' + name)
        # всегда храним название рабочей папки в одном и том же месте
        # чтобы при любых изменениях читать нужную запись
        with open(os.path.dirname(os.path.abspath(__file__)) + '_.wfolder', 'w', encoding='utf-8') as f:
            f.write(os.getcwd())
    except FileNotFoundError:
        print('Такой папки не существует!')
    else:
        print('Новая рабочая папка:', os.getcwd())
        save_info('Начало')
