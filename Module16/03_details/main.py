shop = [['каретка', 1200], ['шатун', 1000], ['седло', 300],
        ['педаль', 100], ['седло', 1500], ['рама', 12000],
        ['обод', 2000], ['шатун', 200], ['седло', 2700]]

# TODO здесь писать код
detail = input('Название детали: ')
count = 0
sum_price = 0
for i in shop:
    for j in i:
        if j == detail:
            count += 1
            sum_price += i[1]
print('Кол-во деталей -', count)
print('Общая стоимость -', sum_price)
