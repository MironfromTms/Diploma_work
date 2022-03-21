# TODO здесь писать код
max_number = int(input('Введите максимальное число: '))
if_yes_set = set()
if_no_set = set()
while True:
    print('Нужное число есть среди вот этих чисел: ', end='')
    numbers = input()
    if numbers == 'Помогите!':
        print('Артём мог загадать следующие числа: ', end='')
        answer = sorted(if_yes_set.difference(if_no_set))
        for i in answer:
            print(i, end=' ')
        break
    print('Ответ Артёма: ', end='')
    answer = input().lower()
    numbers_list = numbers.split()
    if answer == 'да':
        if_yes_set.update(numbers_list)
    elif answer == 'нет':
        if_no_set.update(numbers_list)

