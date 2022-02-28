# TODO здесь писать код
file_name = input('Название файла:')
error_symbols = '@№$%^&*()'
files_ends = ['.txt, .docx']
for i_sym in error_symbols:
    if file_name.startswith(i_sym):
        print('Ошибка: название начинается на один из специальных символов')
for i_sym in files_ends:
    if file_name.endswith(i_sym):
        print('Ошибка: неверное расширение файла. Ожидалось .txt или .docx')

print('Файл назван верно.')
