import os

print (os.getcwd())
def create_dir():
    for i in range(1,10):
        try:
            new_path = os.path.join(os.getcwd(), f'dir_{i}')
            os.mkdir(new_path)
        except FileExistsError:
            print('Папка',f'dir_{i}', 'уже существует')
def delete_dir():
    for i in range(1, 10):
        try:
            new_path = os.path.join(os.getcwd(), f'dir_{i}')
            os.rmdir(new_path)
        except FileNotFoundError:
            print('Папка', f'dir_{i}', 'не существует')
