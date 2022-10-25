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
        self.house.fridge.food -= 10
        self.satiety += 10

    def work(self):
        self.satiety -= 10
        self.house.locker.money += 10

    def play_the_game(self):
        self.satiety -= 10

    def go_to_the_shop(self):
        self.house.fridge.food += 10
        self.house.locker.money -= 10

    def act(self):
        random_number = random.randint(0, 6)
        self.show_me_the_info()
        if self.satiety < 20:
            self.eat_the_food()
            print(f'{self.name} is hungry! Let is go for an eating!')
        elif self.house.fridge.food < 10:
            self.go_to_the_shop()
            print(f'Not enough food!{self.name} going to the shop!')
        elif self.house.locker.money < 50:
            self.work()
            print(f'Not enough money!{self.name} go to the work!')
        elif random_number == 1:
            self.work()
            print(f'{self.name} go for the work!')
        elif random_number == 2:
            self.eat_the_food()
            print(f'{self.name} is eating!')
        elif random_number in [3, 4, 5, 6]:
            self.play_the_game()
            print(f'{self.name} playing the game!')
        elif self.satiety < 0:
            print(f'{self.name} now is dead! Try to eat more food next time!')


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
first_house = House()
second_house = House()
first_human = Human('Petr', satiety=50, house=first_house)
second_human = Human('Jim', satiety=50, house=second_house)

days = 1
for i_day in range(366):
    print(f'It is {i_day} day!')
    first_human.act()
    second_human.act()
