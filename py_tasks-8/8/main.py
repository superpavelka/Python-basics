import sys
import os
from core import create_file, create_folder, get_list, delete_file, copy_file, save_info, change_folder
from game import guess_the_number

try:
    with open(os.path.dirname(os.path.abspath(__file__)) + '_.wfolder', 'r', encoding='utf-8') as f:
        dir_name = f.readline()
        if dir_name:
            if (os.path.isdir(dir_name)):
                os.chdir(dir_name)
            else:
                print('Установленная ранее рабочая папка не существует или запись о ней была исорчена!')
except FileNotFoundError:
    pass

save_info('Начало')
print('Рабочая папка:', os.getcwd())
try:
    command = sys.argv[1]
except IndexError:
    print('Введите команду исполнения для скрипта!')
    command = 'help'

if command == 'list':
    get_list()
elif command == 'create_file':
    try:
        name = sys.argv[2]
    except IndexError:
        print('Отсутствует название файла!')
    else:
        try:
            text = sys.argv[3]
        except IndexError:
            create_file(name)
        else:
            create_file(name, sys.argv[3])
elif command == 'create_folder':
    try:
        name = sys.argv[2]
    except IndexError:
        print('Отсутствует название папки!')
    else:
        create_folder(name)
elif command == 'delete':
    try:
        name = sys.argv[2]
    except IndexError:
        print('Отсутствует название файла!')
    else:
        delete_file(name)
elif command == 'copy':
    try:
        name = sys.argv[2]
    except IndexError:
        print('Отсутствует название копируемого файла!')
    try:
        new_name = sys.argv[3]
    except IndexError:
        print('Отсутствует название копии файла!')
    else:
        if (name != new_name):
            copy_file(name, new_name)
        else:
            print('Имя копируемого объекта и копии должны различаться!')
elif command == 'cd':
    try:
        name = sys.argv[2]
    except IndexError:
        print('Отсутствует название директории!')
    else:
        change_folder(name)
elif command == 'play':
    guess_the_number()
    save_info('Пользователь играл в игру')
elif command == 'help':
    print('list - список файлов и папок')
    print('create_file [название файла] [текст для ввода в файл(необязательно)] - создание файла')
    print('create_folder [название папки] - создание папки')
    print('delete [название объекта]- удаление файла или папки')
    print('copy [название копируемого объекта] [название копии объекта]- копирование файла или папки')
    print('cd [название директории] - сменить рабочую директорию(используйте .. чтобы подняться на уровень выше)')
    print('play - сыграть с компьютером в игру "угадай число"')
else:
    print('Недопустимая команда! Для просмотра допустимых команд введите help')

save_info('Конец')
