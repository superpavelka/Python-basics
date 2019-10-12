fruits1 = ['Банан', 'Апельсин', 'Ананас', 'Алыча','Лайм']
fruits2 = ['Авокадо', 'Ананас', 'Апельсин', 'Персик','Лайм']

result = [number for number in fruits1 if number in fruits2]
print(result)