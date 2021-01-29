amount = int(input('Кол-во контейнеров:'))
full_list = []
while amount > 0:
    amount -= 1
    weight = int(input('Введите вес контейнера: '))
    if weight > 200:
        print('недопустимый вес контейнера! Введите число до 200 кг')
    else:
        full_list.append(weight)
print(full_list)
new_weight = int(input('Введите вес нового контейнера: '))
if new_weight > 200:
    print('недопустимый вес контейнера! Введите число до 200 кг')
