# TODO здесь писать код
def score_key(user_list):
    return int(user_list[1][0]) * 100000000 - int(user_list[1][1])


number_of_records = int(input('Сколько записей вносится в протокол? '))
print('Записи (результат и имя):')
score_dict = dict()
for i_record in range(number_of_records):
    print(i_record + 1, 'запись:', end='')
    player_score = input('')
    player_score_list = player_score.split()
    if player_score_list[1] not in score_dict:
        score_dict[player_score_list[1]] = [player_score_list[0], i_record]
    else:
        if int(score_dict[player_score_list[1]][0]) < int(player_score_list[0]):
            score_dict[player_score_list[1]] = [player_score_list[0], i_record]

while True:
    if len(score_dict.keys()) < 3:
        print('Не достаточное количество игроков. Соревнования не действительны! ')
        break

    scores = list(score_dict.items())
    scores.sort(key=score_key, reverse=True)

    print('Итоги соревнований:')
    for i_place in range(3):
        print(i_place + 1, "место: ", end='')
        print(scores[i_place][0], (scores[i_place][1][0]))
    break
