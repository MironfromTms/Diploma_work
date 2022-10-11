# TODO здесь писать код
user_text_str =''
user_text = open('text.txt', 'w')
user_text.write('Mama myla ramu.')
user_text.close()
user_text = open('text.txt', 'r')
for i_word in user_text:
    user_text_str += i_word
print('Содержимое файла text.txt:')
print(user_text_str)


def histogram(string):
    sym_dict = dict()
    for sym in string:
        if sym in sym_dict and sym.isalpha():
            sym_dict[sym] += 1
        else:
            sym_dict[sym] = 1

    return sym_dict


print()
print('Содержимое файла analysis.txt:')
hist = histogram(user_text_str.lower())
analysis_text = open('analysis.txt', 'w')
for i_sym in sorted(hist.keys()):
    if i_sym.isalpha():
        analysis_text.write(i_sym +' ' + str(round(hist[i_sym]/len(user_text_str), 3)) + '\n')
analysis_text.close()
analysis_text = open('analysis.txt', 'r')
for i_elem in analysis_text.read():
    print(i_elem, end='')
analysis_text.close()