# TODO здесь писать код
def histogram(string):
    sym_dict = dict()
    for sym in string:
        if sym in sym_dict:
            sym_dict[sym] += 1
        else:
            sym_dict[sym] = 1

    return sym_dict


text = input('Введите текст: ').lower()
print()
print('Оригинальный словарь частот:')
hist = histogram(text)
for i_sym in sorted(hist.keys()):
    print(i_sym, ':', hist[i_sym])

new_dict = dict()
for i in hist.keys():
    value = hist[i]
    if value not in new_dict:
        new_dict[value] = []
    new_dict[value].append(i)
print()
print('Инвертированный словарь частот:')
for i in new_dict.keys():
    print(i, ':', new_dict[i])
