# TODO здесь писать код
rollers_count = int(input('Кол-во коньков: '))
pair_size_list = []
while rollers_count > 0:
    for i in range(rollers_count):
        print('Введите размер', i + 1, 'пары:', end=' ')
        pair = int(input())
        pair_size_list.append(pair)
        rollers_count -= 1

print(pair_size_list)

people_count = int(input('Кол-во людей:'))
people_size_list = []
while people_count > 0:
    people_count -= 1
    for i in range(people_count):
        print('Размер ноги ', i + 1, 'человека:', end='')
        size = int(input())
        people_size_list.append(size)
print(people_size_list)

mach_counter = 0
for i in pair_size_list:
    if i in pair_size_list:
        mach_counter += 1
        pair_size_list.remove(i)
print('Наибольшее кол-во людей, которые могут взять ролики: ', mach_counter)
