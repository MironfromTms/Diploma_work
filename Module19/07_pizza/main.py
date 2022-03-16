# TODO здесь писать код
orders_number = int(input('Введите кол-во заказов: '))
orders_dict = dict()
for i in range(1, orders_number + 1):
    print(i, 'заказ: ', end='')
    surname, pizza, quantity = input().split()
    if surname not in orders_dict:
        orders_dict[surname] = {pizza: int(quantity)}
    else:
        if pizza not in orders_dict[surname]:
            orders_dict[surname][pizza] = int(quantity)
        else:
            orders_dict[surname][pizza] += int(quantity)

for i in orders_dict:
    print(i, ':')
    for j in orders_dict[i]:
        print('        ', j, ':', orders_dict[i][j])
