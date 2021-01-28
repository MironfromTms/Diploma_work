word = input('Введите слово: ')
world_list = list(word)
reversed_word = []
for i in reversed(world_list):
    reversed_word.append(i)
if world_list == reversed_word:
    print('Слово является палиндромом')
else:
    print('Слово не является палиндромом')