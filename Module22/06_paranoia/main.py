# TODO здесь писать код
alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
def ceasar_cipher(string, user_step):
    char_list = [(alphabet[(alphabet.index(sym) + user_step) % 66] if sym != ' ' else ' ') for sym in string]
    new_str = ''
    for i_char in char_list:
        new_str += i_char
    return new_str


print('Содержимое файла text.txt:')
step = 0
str_text = []
old_text = open('text', 'r', encoding='utf=8')
for i_word in old_text:
    str_text.append(i_word[0:5])
    print(i_word, end='')
str_text.pop()
old_text.close()
print('Содержимое файла cipher_text.txt:')
for j_word in str_text:
    step += 1
    print(ceasar_cipher(j_word, step))

