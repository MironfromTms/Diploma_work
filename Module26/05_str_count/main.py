# TODO здесь писать код
import os


def str_counter(directory):
    for root, dirs, files in os.walk(directory):
        for file in files:
            count = 0
            if os.path.join(root, file).endswith('.py'):
                curr_file = open(os.path.join(root, file), 'r', encoding='utf-8')
                for line in curr_file.readlines():
                    if not (line == '\n' or line.strip().startswith(('"', '#', "'"))):
                        count += 1
                yield os.path.join(root, file), count


for i_element in str_counter(directory='..'):
    print(f'File "{i_element[0]}": lines of code - {i_element[1]}')
