# TODO здесь писать код
countries = int(input('Кол-во стран: '))
country_dict = dict()
for i in range(1, countries + 1):
    print(i, 'страна: ', end='')
    country = input()
    country_info = country.split()
    for j in country_info[1:]:
        country_dict[j] = country_info[0]

print()

for i in range(1, 4):
    print(i, 'город: ', end='')
    city = input()
    if city in country_dict:
        print('Город', city, 'расположен в стране', country_dict[city])
    else:
        print('По городу', city, 'данных нет.')
