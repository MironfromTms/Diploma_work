# TODO здесь писать код
first_tour = open('first_tour.txt', 'r', encoding='utf=8')
first_tour_list = []
i_word_str = ''
for i_word in first_tour.read():
    i_word_str += i_word
first_tour_list = i_word_str.split('\n')
print(i_word_str)
score_to_pass = first_tour_list[0]
second_tour_list = []
for i_man in first_tour_list[1:int(len(first_tour_list) + 1)]:
    for i_score in i_man.split():
        if i_score.isdigit():
            if i_score > score_to_pass:
                second_tour_list.append(i_man)
first_tour.close()
print('Содержимое файла second_tour.txt:')
numeration = 0
second_tour = open('second_tour.txt', 'w', encoding='utf=8')
second_tour.write(str(len(second_tour_list)) + '\n')
for i_man in sorted(second_tour_list):
    numeration += 1
    i_man_list = list(i_man.split())
    i_man_str = str(numeration) + ') ' + i_man_list[1][:1] + '. ' + i_man_list[0] + ' ' + i_man_list[2] +'\n'
    second_tour.write(i_man_str)
second_tour.close()
second_tour = open('second_tour.txt', 'r')
for i_element in second_tour.read():
    print(i_element, end='')
