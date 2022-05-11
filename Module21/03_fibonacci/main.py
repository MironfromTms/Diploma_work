# TODO здесь писать код
def position_fibonacci(number):
    if number == 1 or number == 2:
        return 1
    return position_fibonacci(number - 1) + position_fibonacci(number - 2)


user_number = int(input('Введите позицию числа в ряде Фибоначчи: '))
print('Число:', position_fibonacci(user_number))
