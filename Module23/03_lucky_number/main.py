# TODO здесь писать код
import random

num_sum = 0
while num_sum <= 777:
    try:
        user_number = int(input('Введите число:'))
        num_sum += user_number
        n = random.randint(1, 13)
        if n == 13:
            raise BaseException
        with open('out_file.txt', 'a') as answer_file:
            answer_file.write(str(user_number) + '\n')
    except BaseException:
        print('Вы потерпели неудачу!')
        break
else:
    print('Вы успешно выполнили условие для выхода из порочного цикла!')
with open('out_file.txt', 'r') as answer_file:
    print('Содержимое файла out_file.txt:')
    for i_line in answer_file:
        print(i_line, end='')