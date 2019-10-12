numbers = [-12, -4, -3, 0 , 1 , 3, 6, 9 , 12, 15, 16]
print('Исходный список', numbers)

result = [number for number in numbers if number % 3 == 0 and number > 0 and number % 4 != 0]
print('Новый список', result)