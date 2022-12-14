# TODO здесь писать код



def add_contact():
    contact_name = input('Введите имя и фамилию нового контакта (через пробел): ')
    name_list = contact_name.split()
    name_tuple = tuple(name_list)
    if name_tuple in phone_book.keys():
        print('Такой контакт уже есть в телефонной книге, попробуйте еще раз.')
    else:
        phone = input('Введите номер телефона: ')
        phone_book[name_tuple] = phone


def search_contact():
    print('Введите фамилию для поиска: ', end='')
    search_surname = input().lower()
    for i_name, i_number in phone_book.items():
        if search_surname == i_name[1].lower():
            print(i_name[0], i_name[1], i_number)
        elif i_name[1][:-1].lower() == search_surname:
            print(i_name[0], i_name[1], i_number)
        else:
            print('Такой фамилии нет в списке контактов.')


phone_book = dict()
while True:
    print('Введите номер действия: ',
          '\n1. Добавить контакт ',
          '\n2. Найти человека')
    choice = int(input())
    if choice == 1:
        add_contact()
        print('Текущий словарь контактов: ', phone_book)
    if choice == 2:
        search_contact()