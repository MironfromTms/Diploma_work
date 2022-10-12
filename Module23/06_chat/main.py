# TODO здесь писать код
user_name = input('Как вас зовут?:')
while True:
    print('Чтобы увидеть текущий текс чата введите 1, чтобы написать сообщение введите 2')
    response = input('Введите 1 или 2')
    if response == 1:
        try:
            with open('chat.txt', 'r') as file:
                massages = file.readline()
                print(''.join(massages))
        except FileNotFoundError:
            print('Служебное сообщение: пока ничего не существует\n')
    elif response == 2:
        new_massage = input('Введите ваше сообщение:')
        with open('chat.txt', 'a') as file:
            file.write('{name}: {massage}\n'.format(name=user_name, massage=new_massage))
    else:
        print('Неизвестная команда!\n')




