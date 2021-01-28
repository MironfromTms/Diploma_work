films = ['Крепкий орешек', 'Назад в будущее', 'Таксист', 'Леон',
         'Богемская рапсодия', 'Город грехов', 'Мементо', 'Отступники', 'Деревня']
favorite_films = []
while True:
    user_film = input('Введите ваш фильм: (для остановки введите - end)')
    if user_film in films:
        favorite_films.append(user_film)
        print(favorite_films)
    elif user_film == 'end':
        break
    else:
        print('Такого фильма нет в списке!')
print('Весь список любимых фильмов', favorite_films)
