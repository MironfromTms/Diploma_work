# TODO здесь писать код
first_list = []
for i in range(3):
    print('Введите', i + 1, 'элемент первого списка: ', end='')
    element = int(input())
    first_list.append(element)
print()
second_list = []
for i in range(7):
    print('Введите', i + 1, 'элемент второго списка: ', end='')
    element = int(input())
    second_list.append(element)
print()
print('Первый список: ', first_list)
print('Второй список: ', second_list)

first_list.extend(second_list)

for i in first_list:
    j = first_list.count(i)
    for _ in range(j-1):
        first_list.remove(i)
print('Новый первый список с уникальными элементами: ', first_list)
