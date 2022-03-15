violator_songs = {
    'World in My Eyes': 4.86,
    'Sweetest Perfection': 4.43,
    'Personal Jesus': 4.56,
    'Halo': 4.9,
    'Waiting for the Night': 6.07,
    'Enjoy the Silence': 4.20,
    'Policy of Truth': 4.76,
    'Blue Dress': 4.29,
    'Clean': 5.83
}

songs_counter = int(input('Сколько песен выбрать? '))
i = 1
total_time = 0
while songs_counter > 0:
    print('Название', i, 'песни: ', end='')
    song_name = input()
    song_time = violator_songs.get(song_name)
    total_time += song_time
    i += 1
    songs_counter -= 1

print('Общее время звучания песен: ', total_time, 'минут')