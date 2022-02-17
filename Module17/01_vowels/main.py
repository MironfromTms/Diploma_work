# TODO здесь писать код
phrase = input('Введите текст:')
vowels = ['а', 'у', 'и', 'е', 'ё', 'ы', 'о', 'э', 'я', 'ю']
vowels_in_phrase = [letter for letter in phrase if letter in vowels]

print('Список гласных букв: ', vowels_in_phrase)
print('Длина списка: ', len(vowels_in_phrase))
