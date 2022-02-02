# TODO здесь писать код
print('Кол-во друзей: ', end='')
friends = int(input())
print('Долговых расписок: ', end='')
receipt = int(input())
i = 1
while receipt < 0:
    receipt -= 1
    print(i, 'расписка')
    print('Кому: ', end='')
    to_who = int(input())
    print('От кого: ', end='')
    from_who = int(input())
    print('Сколько: ', end='')
    loan = int(input())
