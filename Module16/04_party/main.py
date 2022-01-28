guests = ['Петя', 'Ваня', 'Саша', 'Лиза', 'Катя']

# TODO здесь писать код

while True:

    print('Сейчас на вечеринке', len(guests), 'человек: ', guests)
    answer = input('Гость пришёл или ушёл? ')
    if answer == 'Пора спать' or answer == 'пора спать':
        print('Вечеринка закончилась, все легли спать.')
        break
    if answer == 'пришёл' or answer == 'пришел':
        name_1 = input('Имя гостя: ')
        guests.append(name_1)
        if len(guests) < 7:
            print('Привет, ', name_1, '!')
        else:
            print('Прости,', name_1, ', но мест нет.')
            guests.remove(name_1)
    if answer == 'ушёл' or answer == 'ушел':
        name_2 = input('Имя гостя: ')
        if name_2 in guests:
            guests.remove(name_2)
            print('Пока,', name_2, '!')