# TODO здесь писать
print('Кол-во человек:', end='')
people = int(input())
print('Какое число в считалке? ', end='')
rhyme_number = int(input())
print('Значит, выбывает каждый', rhyme_number, 'человек')
people_list = []
print()

for i in range(people):
    people_list.append(i + 1)

print('Текущий круг людей:', people_list)
print('Начало счёта с номера ', people_list[0])
print('Выбывает человек под номером ', rhyme_number % len(people_list))
people_list.remove(people_list[rhyme_number % len(people_list)-1])
print()

while len(people_list) > 1:
    out = rhyme_number % len(people_list)-1
    if out == 0:
        print('Текущий круг людей:', people_list)
        print('Начало счёта с номера ', people_list[out])
        print('Выбывает человек под номером ', people_list[out])
        people_list.remove(people_list[out])
        print()
    else:
        print('Текущий круг людей:', people_list)
        print('Начало счёта с номера ', people_list[out-1])
        print('Выбывает человек под номером ', people_list[out]+1)
        people_list.remove(people_list[out]+1)
        print()
print('Остался человек под номером ', people_list[0])