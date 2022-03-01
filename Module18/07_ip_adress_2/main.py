# TODO здесь писать код

ip_address = input('Введите IP: ')
dots_counter = 0

for i in ip_address:
    if i == '.':
        dots_counter += 1

if dots_counter != 3:
    print('Адрес - это четыре числа, разделенные точками')

ip_list = ip_address.split('.')

for i in ip_list:
    if not i.isdigit():
        print(i, '- не целое число')
        break
    elif int(i) > 255:
        print(i, 'превышает 255')
        break
else:
    print('IP-адрес корректен')


