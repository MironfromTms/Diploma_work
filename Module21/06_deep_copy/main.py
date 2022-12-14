site = {
    'html': {
        'head': {
            'title': 'Куплю/продам телефон недорого'
        },
        'body': {
            'h2': 'У нас самая низкая цена на iphone',
            'div': 'Купить',
            'p': 'продать'
        }
    }
}


def find_key(struct, key, name):
    if key in struct:
        struct[key] = name
        return site

    for sub_struct in struct.values():
        if isinstance(sub_struct, dict):
            result = find_key(sub_struct, key, name)
            if result:
                return site


number_of_sites = int(input('Сколько сайтов:'))
for _ in range(number_of_sites):
    product_name = input('Введите название продукта для нового сайта: ')
    key = {'title': f'Куплю/продам {product_name} недорого', 'h2': f'У нас самая низкая цена на {product_name}'}
    for i in key:
        find_key(site, i, key[i])

    print(f'Сайт для {product_name}:')
    print(site, '\n')
