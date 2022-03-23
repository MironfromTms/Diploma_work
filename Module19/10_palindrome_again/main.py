# TODO здесь писать код
def is_polyndrom(string):
    char_dict = dict()
    for i in string:
        char_dict[i] = char_dict.get(i, 0) + 1

    odd_count = 0
    for j in char_dict.values():
        if j % 2 != 0:
            odd_count += 1

    return odd_count <= 1


phrase = input('Введите строку: ')
if is_polyndrom(phrase):
    print('Можно сделать палиндромом')
else:
    print('Нельзя сделать палиндромом')
