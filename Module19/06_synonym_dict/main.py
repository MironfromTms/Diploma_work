# TODO здесь писать код
counter = int(input('Введите количество пар слов: '))
words_dict = dict()
for i in range(1, counter + 1):
    print(i, ' пара:', end='')
    pair = input().lower()
    pair_list = pair.split()
    for i_sym in pair_list:
        if not i_sym.isalpha():
            pair_list.remove(i_sym)
    for j in pair_list[1:]:
        words_dict[j] = pair_list[0]

while True:
    new_word = input('Введите слово: ').lower()
    if new_word not in words_dict.keys() not in words_dict.values():
        print('Такого слова в словаре нет.')
        continue
    else:
        answer = words_dict[new_word]
        print('Синоним:', answer.capitalize())
        break