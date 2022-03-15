goods = {
    'Лампа': '12345',
    'Стол': '23456',
    'Диван': '34567',
    'Стул': '45678',
}

store = {
    '12345': [
        {'quantity': 27, 'price': 42},
    ],
    '23456': [
        {'quantity': 22, 'price': 510},
        {'quantity': 32, 'price': 520},
    ],
    '34567': [
        {'quantity': 2, 'price': 1200},
        {'quantity': 1, 'price': 1150},
    ],
    '45678': [
        {'quantity': 50, 'price': 100},
        {'quantity': 12, 'price': 95},
        {'quantity': 43, 'price': 97},
    ],
}

# TODO здесь писать код
for good, index in goods.items():
    sum_quantity = 0
    sum_price = 0
    for goods in store[index]:
        good_quantity = goods['quantity']
        good_price = goods['price']
        total_price = good_quantity * good_price
        sum_quantity += good_quantity
        sum_price += total_price
    print(good, '-', sum_quantity, 'шт, стоимостью', sum_price, 'руб')


