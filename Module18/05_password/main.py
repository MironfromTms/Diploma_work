# TODO здесь писать код
while True:
    password = input('Придумайте пароль:', )
    num_counter = 0
    upper_count = 0
    for i_num in password:
        if i_num.isdigit():
            num_counter += 1
    for i_let in password:
        if i_let.isupper():
            upper_count += 1
    if len(password) > 8 and upper_count > 0 and num_counter >= 3:
        print('Это надёжный пароль!')
        break
    else:
        print('Пароль ненадёжный. Попробуйте ещё раз.')


