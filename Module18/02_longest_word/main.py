# TODO здесь писать код
text = input('Введите строку:').split()
maximum = 0
maximum_word = []
for i_text in text:
    if len(i_text) > maximum:
        maximum_word = i_text
print('Самое длинное слово:', maximum_word)
print('Длина этого слова:', len(maximum_word))

