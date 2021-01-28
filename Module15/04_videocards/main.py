video_cards = int(input('Кол-во видеокарт: '))
video_cards_list = []
for i in range(video_cards):
    print(i + 1, 'Видеокарта: ', end='')
    a = int(input())
    video_cards_list.append(a)
print('Старый список видеокарт: ', video_cards_list)
maximum = 0
new_video_cards = []
for i in video_cards_list:
    if i > maximum:
        maximum = i
for j in video_cards_list:
    if j != maximum:
        new_video_cards.append(j)
print('Новый список видеокарт: ', new_video_cards)

