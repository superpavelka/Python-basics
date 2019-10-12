def get_str(name_, age_, city_):
    return name +', ' + age +', год(а), проживает в городе ' + city

name = input('Введите имя: ')

while True:
    age = input('Введите возраст: ')
    try:
        if int(age) < 0 or int(age) > 200:
            print('Ошибка ввода возраста!')
        else:
            break
    except ValueError:
        print('Ошибка ввода числа!')

city = input('Введите название города: ')

print(get_str(name, age, city))