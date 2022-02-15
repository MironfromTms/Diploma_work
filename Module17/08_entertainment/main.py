# TODO здесь писать код
import random

sticks = int(input('Кол-во палок: '))
runs = int(input('Кол-во бросков: '))
sticks_list = ['I' for x in range(sticks)]
i = 1
print(sticks_list)
while runs >= 1:
    runs -= 1
    start = random.randint(1, 10)
    stop = random.randint(start, 10)
    for j in range(start - 1, stop):
        sticks_list[j] = '.'
    print('Бросок ', i, '.Сбиты палки с номера ', start, 'по номер ', stop)
    i += 1

result_list = ''.join(sticks_list)
print('Результат: ', result_list)
