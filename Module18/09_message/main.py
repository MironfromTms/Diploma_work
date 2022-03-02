
def reversed_word(word):
    buffer = []
    result = []
    for i in word:
        if i.isalpha():
            buffer.append(i)
        else:
            rev_buffer = buffer[::-1]
            result.append(rev_buffer)
            result.append(i)
            buffer = []
    open_result = [j for i in result for j in i]
    str_result = ''.join(open_result)
    print(str_result)



word = input('Сообщение: ')
print('Новое сообщение: ', end='')
reversed_word(word)