my_list_1 = [2, 2, 5, 12, 8, 2, 12, 9, 10, 11, 10, 11, 6, 202, 6]
# сортируем список
my_list_1.sort()
print(my_list_1)
i = 0
isRepeat = False;
first_entry = -1;
# перебираем с первого по предпоследний
while i < len(my_list_1) - 1:
    # если текущий равен следущему
    if int(my_list_1[i]) == int(my_list_1[i+1]):
        # удаляем следущий
        my_list_1.remove(my_list_1[i+1])
        # запоминаем что был повтор и его позицию
        if isRepeat != True :
            first_entry = i
        isRepeat = True
        # если не равен двигаем позицию
    else:
        i += 1
        if isRepeat:
            # если все повторы были удалены удаляем его первое вхождение
            my_list_1.remove(my_list_1[first_entry])
            isRepeat = False
            i-=1
# если мы на последнем элементе списка и с ним был повтор удаляем его
if i == len(my_list_1)- 1 and isRepeat:
    my_list_1.remove(my_list_1[first_entry])
print(my_list_1)