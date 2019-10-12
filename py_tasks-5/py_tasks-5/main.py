#Вариант импорта функций по-отдельности
#from mydir import create_dir, delete_dir
#from rand_elem import get_random_elem

import mydir
import rand_elem

elements = [1,2,3,4,5]
mydir.create_dir()
mydir.delete_dir()
print(rand_elem.get_random_elem(elements))
