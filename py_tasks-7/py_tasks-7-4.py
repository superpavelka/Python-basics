def square_f(value):
    if value == 13:
        raise ValueError('Ошибка! Число не может равняться 13!')
    if value < 1 or value > 100:
        raise ValueError('Ошибка! Число должно лежать в пределах от 1 до 100!')
    return value**2

while True:
    try:
        value = int(input('Введите число от 1 до 100 не равное 13: '))
        result = square_f(value)
        print(f'Квадрат числа {value} равен {result}')
        break
    except ValueError:
        print('Ошибка ввода. Необходимо ввести число от 1 до 100 не равное 13.')
