import random


class Human:
    def __init__(self, name, satiety, house):
        self.name = name
        self.satiety = satiety
        self.house = house

    def show_me_the_info(self):
        print(
            f'Satiety now - {self.satiety}. '
            f'Money now - {self.house.locker.money}.'
            f'Food now - {self.house.fridge.food}')

    def eat_the_food(self):
        user_house.fridge.food -= 10
        human.satiety += 10

    def work(self):
        human.satiety -= 10
        user_house.locker.money += 10

    def play_the_game(self):
        human.satiety -= 10

    def go_to_the_shop(self):
        user_house.fridge.food += 10
        user_house.locker.money -= 10


class House:
    def __init__(self):
        self.fridge = fridge
        self.locker = locker


class Fridge:
    def __init__(self, food=50):
        self.food = food


class Locker:
    def __init__(self, money=0):
        self.money = money


fridge = Fridge()
locker = Locker()
user_house = House()
human = Human('Petr', satiety=50, house=user_house)

days = 1
while days < 366:
    print(f'It is {days} day!')
    days += 1
    random_number = random.randint(0, 6)
    human.show_me_the_info()
    if human.satiety < 20:
        human.eat_the_food()
        print(f'{human.name} is hungry! Let is go for an eating!')
    elif user_house.fridge.food < 10:
        human.go_to_the_shop()
        print(f'Not enough food!{human.name} going to the shop!')
    elif user_house.locker.money < 50:
        human.work()
        print(f'Not enough money!{human.name} go for to the work!')
    elif random_number == 1:
        human.work()
        print(f'{human.name} go for the work!')
    elif random_number == 2:
        human.eat_the_food()
        print(f'{human.name} is eating!')
    elif random_number in [3, 4, 5, 6]:
        human.play_the_game()
        print(f'{human.name} playing the game!')
    elif human.satiety < 0:
        print(f'{human.name} now is dead! Try to eat more food next time!')
