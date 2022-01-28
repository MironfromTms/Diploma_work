shop = [['каретка', 1200], ['шатун', 1000], ['седло', 300],
        ['педаль', 100], ['седло', 1500], ['рама', 12000],
        ['обод', 2000], ['шатун', 200], ['седло', 2700]]

# TODO здесь писать код
detail_name = input('Название детали: ')
detail_count = 0
sum_price = 0
for detail in shop:
        if detail[0] == detail_name:
                detail_count += 1
                sum_price += detail[1]
print('Кол-во деталей -', detail_count)
print('Общая стоимость -', sum_price)
