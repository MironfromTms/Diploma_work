import os.path
# Users aa PycharmProjects python_basic Module22 05_save
user_str = input('Введите строку:')
user_path_text =input('Куда хотите сохранить документ? Введите последовательность папок (через пробел):')
file_name = input('Введите имя файла:')
file_path = os.path.join('/Users/aa/PycharmProjects/python_basic/Module22/05_save', file_name)
print(file_path)
if os.path.exists(file_path):
    print('Вы действительно хотите перезаписать файл?')
    user_answer = input().lower()
    if user_answer == 'да' or user_answer == 'yes':
        user_file = open(file_path, 'w')
        user_file.write(user_str)
        user_file.close()
        print('Файл успешно перезаписан!')
    else:
        print('Файл остался без изменений.')
else:
    user_file = open(file_path, 'w')
    user_file.write(file_path)
    user_file.close()
print('Файл успешно сохранен!')
print('Содержимое файла', file_name, '.txt :')
user_file = open(file_name, 'r', encoding='utf=8')
print(user_file.read())
