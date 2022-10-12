# TODO здесь писать код
result = 0
line_count = 0

with open('people.txt', 'r', encoding='utf8') as people:
    for i_line in people:
        line_len = len(i_line)
        result += line_len
        if i_line.endswith('\n'):
            result -= 1
            line_count += 1
            try:
                if line_len <= 3:
                    raise TypeError
            except TypeError:
                print('Ошибка: менее трёх символов в строке {}.'.format(line_count))
print('Общее количество символов: ', result)
