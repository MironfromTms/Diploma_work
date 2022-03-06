
def ceasar_cipher(string):
    char_list = [(alphabet[(alphabet.index(sym) - 1) % 52] if sym.isalpha() else ' ') for sym in string]
    new_str = ''
    for i_char in char_list:
        new_str += i_char
    return new_str


def shift(string, step):
    string_list = string.split()
    new_string = []
    for i_word in string_list:
        if len(i_word) < step:
            new_step = step % len(i_word)
            new_word = i_word[-new_step:] + i_word[:-new_step]
        else:
            new_word = i_word[-step:] + i_word[:-step]
        new_string.append(new_word)
    return new_string




message = 'vujgvmCfb tj ufscfu ouib z/vhm jdjuFyqm jt fscfuu uibo jdju/jnqm fTjnqm tj scfuuf ibou fy/dpnqm yDpnqmf jt cfuufs boui dbufe/dpnqmj uGmb tj fuufsc ouib oftufe/ bstfTq jt uufscf uibo otf/ef uzSfbebcjmj vout/dp djbmTqf dbtft (ubsfo djbmtqf hifopv up csfbl ifu t/svmf ipvhiBmu zqsbdujdbmju fbutc uz/qvsj Fsspst tipvme wfsof qbtt foumz/tjm omfttV mjdjumzfyq odfe/tjmf Jo fui dfgb pg hvjuz-bncj gvtfsf fui ubujpoufnq up ftt/hv Uifsf vmetip fc pof.. boe sbcmzqsfgf zpom pof pvt..pcwj xbz pu pe ju/ Bmuipvhi uibu bzx bzn puo cf wjpvtpc bu jstug ttvomf sfzpv( i/Evud xOp tj scfuuf ibou /ofwfs uipvhiBm fsofw jt fopgu cfuufs boui iu++sjh x/op gJ ifu nfoubujpojnqmf tj eibs pu mbjo-fyq tju( b bec /jefb Jg fui foubujpojnqmfn jt fbtz up bjo-fyqm ju znb cf b hppe jefb/ bnftqbdftO bsf pof ipoljoh sfbuh efbj .. fu(tm pe psfn gp tf"uip'
alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
message_list = message.split()
buffer = []
answer = []
for i_word in message_list:
    buffer.append(i_word)
    if '/' in i_word:
        str_buffer = ' '.join(buffer)
        answer.append(str_buffer)
        buffer = []
print('Зашифрованная строка: ')
step = 3
for i in answer:
    str_i = ''.join(i)
    beauty = shift(str_i, step)
    beaty_answer = ' '.join(beauty)
    uncode_answer = ceasar_cipher(beaty_answer)
    step += 1
    print(uncode_answer)

