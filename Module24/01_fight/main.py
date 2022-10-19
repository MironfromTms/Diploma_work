# TODO здесь писать код
# TODO здесь писать код
import random


class Warrior:
    def __int__(self, health):
        self.health = health


first_warrior = Warrior()
first_warrior.health = 100
second_warrior = Warrior()
second_warrior.health = 100

while True:
    if random.randint(1, 2) == 1:
        second_warrior.health -= 20
        print('Атаку провел первый воин! Здоровье второго воина :', second_warrior.health)
        if second_warrior.health <= 0:
            print('Первый воин победил! У него осталось: {} очков здоровья'.format(first_warrior.health))
            break
    else:
        first_warrior.health -= 20
        print('Атаку провел второй воин! Здоровье первого воина :', first_warrior.health)
        if first_warrior.health <= 0:
            print('Второй воин победил! У него осталось: {} очков здоровья'.format(second_warrior.health))
            break

