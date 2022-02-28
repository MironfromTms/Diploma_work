# TODO здесь писать код
phrase = list(input('Введите строку: '))
count = 1
new_phrase = []
for i in range(1, len(phrase)):
    if phrase[i-1] == phrase[i]:
        count += 1
    else:
        new_phrase.append(phrase[i-1])
        new_phrase.append(str(count))
        count = 1
new_phrase.append(phrase[-1])
new_phrase.append(str(count))
print('Новое сообщение: ', ''.join(new_phrase))