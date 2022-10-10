# TODO здесь писать код
import os.path

user_path = '/Users/aa/PycharmProjects/python_basic'
print('Исследуемый каталог:', user_path)
size = 0
files_counter = 0
dirs_counter = 0
for i_path in os.listdir(user_path):
    first_path = os.path.join(user_path, i_path)
    if os.path.isfile(first_path):
        files_counter += 1
        size += os.path.getsize(first_path)
    else:
        dirs_counter += 1
        for j_path in os.listdir(first_path):
            if os.path.isfile(os.path.join(j_path)):
                files_counter += 1
                size += os.path.getsize(j_path)
            elif os.path.isdir(j_path):
                dirs_counter += 1

kbt_size = round(size / 1024, 2)
print('Размер каталога (в Кб):', kbt_size)
print('Количество подкаталогов:', dirs_counter)
print('Количество файлов:', files_counter)
