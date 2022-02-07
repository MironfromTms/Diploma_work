# TODO здесь писать код
import random

team_1 = [round(random.uniform(5, 10), 2) for _ in range(20)]
team_2 = [round(random.uniform(5, 10), 2) for _ in range(20)]
winners = [(team_1[x] if team_1[x] > team_2[x]
            else team_2[x]) for x in range(20)]
print('Первая команда: ', team_1)
print('Вторая команда: ', team_2)
print('Победители тура: ', winners)
