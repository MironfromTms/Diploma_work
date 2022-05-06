def num_count(number):
    if number == 0:
        return 1
    num_count(number - 1)
    print(number)


user_number = int(input('Введите num: '))
num_count(user_number)
