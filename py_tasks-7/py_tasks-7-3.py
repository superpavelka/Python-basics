import math

# функция sqrt возвращает число с плавающей точкой, поэтому,
# чтобы было как в примере к заданию, приводим к целому числу
def list_sort (numbers_list):
    return [int(math.sqrt(number)) if number > 0 else number for number in old_list]

# если в списке будут числа, корень которых не является целым числом
def list_sort_fract (numbers_list):
    return [round(math.sqrt(number),2) if number > 0 else number for number in old_list]

old_list = [1, -3, 4, -8, 9, -10, 0]
print('Исходный список', old_list)

result = list_sort(old_list)
print('Новый список', result)
print('Исходный список не изменился', old_list)


old_list = [3, -3, 4, -8, 5, -10]
print('Список с числами, корень которых не является целым числом', old_list)
result = list_sort_fract(old_list)
print('Новый список',result)
print('Исходный список не изменился', old_list)
