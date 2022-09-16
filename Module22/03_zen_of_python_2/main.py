# TODO здесь писать код
zen_text = open('zen.txt', 'r', encoding='utf8')
zen_text_list = []
str_counter = 0
words_counter = 0
letters_counter = 0
unique_letters = []
for i_str in zen_text:
    zen_text_list.append(i_str)
    str_counter += 1
    i_str_list = i_str.split()
    for i_word in i_str_list:
        words_counter += 1
        for i_letter in i_word:
            if i_letter.isalpha():
                letters_counter += 1
                if i_letter.lower() not in unique_letters:
                    unique_letters.append(i_letter)

print('Количество строк в файле: ', str_counter)
print('Количество слов в файле: ', words_counter)
print('Количество букв в файле: ', letters_counter)
print('Количество уникальных букв в файле: ', len(unique_letters))
