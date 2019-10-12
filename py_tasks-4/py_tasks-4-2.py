numbers = []
def number_input():
    while True:
        try:
            number = int(input('Введите число: '))
            numbers.append(number)
            break
        except ValueError:
            print('Ошибка ввода числа!')

def max_number(numbers):
    return max(numbers)

for i in range(3):
    number_input()

print('Максимальное число равно: ', max_number(numbers))