my_list_1 = [6, 5, 8, 2, 7, 7, 4]
my_list_2 = [6, 7, 7, 8, 4]
# можем выдать на печать
print(set(my_list_1) - set(my_list_2))
# можем запихнуть в переменную и после распечатать
lst_diff = set(my_list_1) - set(my_list_2)
print(lst_diff)
# можно привести к листу и снова его напечатать
lst_diff = list(lst_diff)
print(type(lst_diff))
print(lst_diff)