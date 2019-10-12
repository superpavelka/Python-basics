import sys
date =  '28.02.1999'
# режем строку по разделителю точка
date_lst = date.split('.')
# приводим к инту чтобы исключить ошибки ввода
day = int(date_lst[0])
month = int(date_lst[1])
year = int(date_lst[2])
# печатаем разрезаннную строку
print(date_lst)
# далее подбираем по номеру нужный текст
if (day > 0 and day < 32):
    if (day == 1):
        sys.stdout.write('Первое')
    elif (day == 2):
        sys.stdout.write('Второе')
    elif (day == 3):
        sys.stdout.write('Третье')
    elif (day == 4):
        sys.stdout.write('Четвертое')
    elif (day == 5):
        sys.stdout.write('Пятое')
    elif (day == 6):
        sys.stdout.write('Шестое')
    elif (day == 7):
        sys.stdout.write('Седьмое')
    elif (day == 8):
        sys.stdout.write('Восьмое')
    elif (day == 9):
        sys.stdout.write('Девятое')
    elif (day == 10):
        sys.stdout.write('Десятое')
    elif (day == 11):
        sys.stdout.write('Одиннадцатое')
    elif (day == 12):
        sys.stdout.write('Двенадцатое')
    elif (day == 13):
        sys.stdout.write('Тринадцатое')
    elif (day == 14):
        sys.stdout.write('Четырнадцатое')
    elif (day == 15):
        sys.stdout.write('Пятнадцатое')
    elif (day == 16):
        sys.stdout.write('Шестнадцатое')
    elif (day == 17):
        sys.stdout.write('Семдадцатое')
    elif (day == 18):
        sys.stdout.write('Восемнадцатое')
    elif (day == 19):
        sys.stdout.write('Девятнадцатое')
    elif (day == 20):
        sys.stdout.write('Двадцатое')
    elif (day == 21):
        sys.stdout.write('Двадцать первое')
    elif (day == 22):
        sys.stdout.write('Двадцать второе')
    elif (day == 23):
        sys.stdout.write('Двадцать третье')
    elif (day == 24):
        sys.stdout.write('Двадцать четвертое')
    elif (day == 25):
        sys.stdout.write('Двадцать пятое')
    elif (day == 26):
        sys.stdout.write('Двадцать шестое')
    elif (day == 27):
        sys.stdout.write('Двадцать седьмое')
    elif (day == 28):
        sys.stdout.write('Двадцать восьмое')
    elif (day == 29):
        if (month == 2) and date_lst[2].isdigit() and int(date_lst[2])%4 == 0:
            sys.stdout.write('Двадцать девятое')
        else:
            sys.stdout.write('Ошибка ввода дня!')
    elif (day == 30):
        if month == 2:
            sys.stdout.write('Ошибка ввода дня!')
        else:
            sys.stdout.write('Тридцатое')
    elif (day == 31):
        if month == 2 or month == 4 or month == 6 or month == 9 or month == 11:
            sys.stdout.write('Ошибка ввода дня!')
        else:
            sys.stdout.write('Тридцать первое')
    else:
        sys.stdout.write('Ошибка ввода дня!')
else:
    sys.stdout.write('Ошибка ввода дня месяца!')
sys.stdout.write(' ')
if (month > 0 and month < 13):
    if (month == 1):
        sys.stdout.write('Января')
    elif (month == 2):
        sys.stdout.write('Февраля')
    elif (month == 3):
        sys.stdout.write('Марта')
    elif (month == 4):
        sys.stdout.write('Апреля')
    elif (month == 5):
        sys.stdout.write('Мая')
    elif (month == 6):
        sys.stdout.write('Июня')
    elif (month == 7):
        sys.stdout.write('Июля')
    elif (month == 8):
        sys.stdout.write('Августа')
    elif (month == 9):
        sys.stdout.write('Сентября')
    elif (month == 10):
        sys.stdout.write('Октября')
    elif (month == 11):
        sys.stdout.write('Ноября')
    elif (month == 12):
        sys.stdout.write('Декабря')
else:
    sys.stdout.write('Ошибка ввода месяца!')
sys.stdout.write(' ')
if (date_lst[2].isdigit() > 0) and (int(date_lst[2]) > 0):
    sys.stdout.write(date_lst[2])
    sys.stdout.write(' ')
    sys.stdout.write('Года')
else:
    sys.stdout.write('Ошибка ввода года!')