# TODO здесь писать код
def ceasar_cipher(string, user_step):
    char_list = [(alphabet[(alphabet.index(sym) + user_step) % 33] if sym != ' ' else ' ') for sym in string]
    new_str = ''
    for i_char in char_list:
        new_str += i_char
    return new_str


alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
input_str = input('Введите строку: ')
step = int(input('Введите шаг сдвига: '))
output_str = ceasar_cipher(input_str, step)

print('Зашифрованная строка: ', output_str)