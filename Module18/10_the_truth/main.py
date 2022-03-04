
def ceasar_cipher(string):
    char_list = [(alphabet[(alphabet.index(sym) + 1) % 52] if sym.isalpha() else '\n') for sym in string]
    new_str = ''
    for i_char in char_list:
        new_str += i_char
    return new_str


def shift(string, step=3):
    string_list = string.split()
    new_string = []
    for i_word in string_list:
        new_word = i_word[-step:] + i_word[:-step]
        new_string.append(new_word)
        if '/' in i_word:
            step += 1
    answer = ' '.join(new_string)
    print()
    return answer


message = 'vujgvmCfb tj ufscfu ouib z/vhm jdjuFyqm jt fscfuu uibo jdju/jnqm fTjnqm tj scfuuf ibou fy/dpnqm '
alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
message_list = message.split()
buffer = []
answer = []
for i_word in message_list:
    buffer.append(i_word)
    if '/' in i_word:
        str_buffer = ' '.join(buffer)
        answer.append(str_buffer)
        buffer = []
for i in answer:
    str_i = ''.join(i)
    beauty = shift(str_i)
    print(beauty)




# print('Зашифрованная строка: ', )