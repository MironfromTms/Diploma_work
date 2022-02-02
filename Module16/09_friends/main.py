# TODO здесь писать код
print('Кол-во друзей: ', end='')
friends = int(input())
print('Долговых расписок: ', end='')
receipt = int(input())
friends_list = []

for _ in range(friends):
    friends_list.append([0, 0])

for i in range(receipt):
    print(i + 1, 'расписка')
    print('Кому: ', end='')
    to_who = int(input())
    print('От кого: ', end='')
    from_who = int(input())
    print('Сколько: ', end='')
    loan = int(input())
    friends_list[to_who - 1][1] += loan
    friends_list[from_who - 1][1] -= loan

print('Баланс друзей:')
for i in range(friends):
    print(i + 1, ':', friends_list[i][1])
