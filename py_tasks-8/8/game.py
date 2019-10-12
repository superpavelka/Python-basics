import random


def guess_the_number():
    print('Загадайте число от 0 до 100 в уме и/или напишите его на бумаге')

    user_input = '<'
    number_min = 0
    number_max = 100
    incorrect_input = False
    is_winner = False
    count = 1

    while not is_winner:
        if (number_min == number_max):
            print(f'Попытка № {count}. Ваше число равно: {number_min}')
            number = number_min
            is_winner = True
            break
        if not incorrect_input:
            number = random.randint(number_min, number_max)
        print(f'Попытка № {count}. Ваше число равно: {number}')
        user_input = input('Введите <, > или = : ')
        if user_input == '<':
            if (number - 1) >= number_min:
                number_max = number - 1
                incorrect_input = False
            else:
                print(f'Число не может быть больше {number_min} и меньше {number} одновременно')
                continue
        elif user_input == '>':
            if (number + 1) <= number_max:
                number_min = number + 1
                incorrect_input = False
            else:
                print(f'Число не может быть больше {number} и меньше {number_max} одновременно')
                continue
        elif user_input == '=':
            is_winner = True
        else:
            print('Вы ввели некорректный символ')
            incorrect_input = True
            continue
        count += 1

    print(f'Загаданное число равно {number}')
