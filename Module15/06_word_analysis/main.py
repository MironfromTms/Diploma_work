word = input('Введите слово: ')
word_list = list(word)
lenght = len(word)
count = 0
for i in word:
    if word_list.count(i) == 1:
        count += 1
print('Кол-во уникальных букв: ', count)