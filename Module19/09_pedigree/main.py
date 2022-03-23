# TODO здесь писать код
people = int(input('Введите количество человек: '))
family_dict = dict()
cointer = 0
for i in range(1, people + 1):
    print(i, 'пара:', end='')
    pair = input()
    pair_list = pair.split()
    if pair_list[1] not in family_dict:
        family_dict[pair_list[1]] = 0
        family_dict[pair_list[0]] = family_dict[pair_list[1]] + 1
    else:
        family_dict[pair_list[0]] = family_dict[pair_list[1]] + 1
print('“Высота” каждого члена семьи:')
for i in sorted(family_dict.keys()):
    print(i, family_dict[i])

