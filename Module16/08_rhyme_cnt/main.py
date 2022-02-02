# TODO здесь писать
print('Кол-во человек:', end='')
people = int(input())
print('Какое число в считалке? ', end='')
rhyme_number = int(input())
print('Значит, выбывает каждый', rhyme_number, 'человек')
print()

people_list = list(range(1, people + 1))
rhyme_number = 7

start = 0
while len(people_list) > 1:
    print('Текущий круг людей:', people_list)
    print('Начало счёта с номера ', people_list[start])
    start += rhyme_number - 1
    start = start % len(people_list)
    print('Выбывает человек под номером ', people_list[start])
    people_list.remove(people_list[start])
    start = start % len(people_list)
    print()
print('Остался человек под номером ', people_list)

