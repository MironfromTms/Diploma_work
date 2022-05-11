# TODO здесь писать код
site = {
    'html': {
        'head': {
            'title': 'Мой сайт'
        },
        'body': {
            'h2': 'Здесь будет мой заголовок',
            'div': 'Тут, наверное, какой-то блок',
            'p': 'А вот здесь новый абзац'
        }
    }
}


def find_key(struct, key, depth=-1):
    if depth < 1:
        return
    if key in struct:
        return struct[key]
    if depth > 1:
        for sub_struct in struct.values():
            if isinstance(sub_struct, dict):
                result = find_key(sub_struct, key, depth - 1)
                if result:
                    break
        else:
            result = None
        return result


user_key = input('Введите искомый ключ: ')
user_answer = input('Хотите ввести максимальную глубину? Y/N:').lower()
if user_answer == 'y':
    user_deep = int(input('Введите максимальную глубину: '))
    print('Значение ключа:', find_key(site, user_key, user_deep))
else:
    print('Значение ключа:', find_key(site, user_key, depth=3))
