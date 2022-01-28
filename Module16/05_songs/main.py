violator_songs = [
    ['World in My Eyes', 4.86],
    ['Sweetest Perfection', 4.43],
    ['Personal Jesus', 4.56],
    ['Halo', 4.9],
    ['Waiting for the Night', 6.07],
    ['Enjoy the Silence', 4.20],
    ['Policy of Truth', 4.76],
    ['Blue Dress', 4.29],
    ['Clean', 5.83]
]

# TODO здесь писать код

count = int(input('Сколько песен выбрать? '))
counter = 0
total_duration = 0
while count > 0:
    count -= 1
    counter += 1
    print('Название', counter, 'песни:', end='')
    song = input()
    for i in violator_songs:
        if song in i:
            total_duration += i[1]
print('Общее время звучания песен: ', total_duration)