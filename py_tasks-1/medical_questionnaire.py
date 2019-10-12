name = input('Введите свое имя:')
surname = input('Введите свою фамилию:')
age = int(input('Введите свой возраст:'))
weight = int(input('Введите свой вес:'))
if (age <= 0) or (weight < 0):
    print(name + ' ' + surname + ',' +
          str(age) + ' ' + 'год,' +
          'вес ' + str(weight)  + ' - следует обратиться к психиатору!')
elif (age > 0) and (age <= 30) and (weight >= 50 and weight <= 120):
    print(name + ' ' + surname + ',' +
          str(age) + ' ' + 'год,' + 'вес ' +
          str(weight) + ' ' + '- хорошее состояние!')
elif (age > 30) and (age <= 40) and (weight < 50 and weight > 120):
    print(name + ' ' + surname + ',' +
          str(age) + ' ' + 'год,' + 'вес ' +
          str(weight) + ' ' +
          '- следует заняться собой')
elif (age > 40) and (weight < 50 or weight > 120):
    print(name + ' ' + surname + ',' +
          str(age) + ' ' + 'год,' + 'вес ' +
          str(weight) + ' ' +
          '- следует заняться собой')
elif (age > 0) and (age <= 14) and (weight < 50):
    print(name + ' ' + surname + ',' +
          str(age) + ' ' + 'год,' + 'вес ' +
          str(weight) + ' ' +
          '- хорошее состояние!')
elif (age > 0) and (age <= 14) and (weight < 50):
    print(name + ' ' + surname + ',' +
          str(age) + ' ' + 'год,' + 'вес ' +
          str(weight) + ' ' +
          '- хорошее состояние!')
else:
    print(name + ' ' + surname + ',' +
          str(age) + ' ' + 'год,' + 'вес ' +
          str(weight) + ' ' +
          '- следует заняться собой')