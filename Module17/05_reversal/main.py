# TODO здесь писать код
phrase = input('Введите строку: ')
start = phrase.index('h')
stop = phrase.rindex('h')
print('Развернутая последовательность между первым и последним h:', phrase[stop - 1:start:-1])
