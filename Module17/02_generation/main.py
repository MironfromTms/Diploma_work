# TODO здесь писать код
len_list = int(input('Введите длину списка: '))
num_list = [(1 if x % 2 == 0
            else x % 5)for x in range(len_list)]

print('Результат: ', num_list)