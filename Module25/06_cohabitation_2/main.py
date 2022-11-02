import random


class HouseResident:
    def __init__(self, name, satiety, happiness=None):
        self.name = name
        self.satiety = satiety
        self.happiness = happiness

    def eat(self):
        house.food -= 30
        self.satiety += 30
        print(f'{self.name} is eating.')


class Husband(HouseResident):
    def __init__(self, name, satiety=30, happiness=100):
        super().__init__(name, satiety, happiness)

    def work(self):
        house.money += 150
        self.satiety -= 10
        print(f'{self.name} is working today.')

    def play_the_game(self):
        self.happiness += 20
        self.satiety -= 10
        print(f'{self.name} play on PS5 and happy.')

    def pet_the_cat(self):
        self.happiness += 5
        self.satiety -= 10
        print(f'{self.name} pet the {Cat.__name__}.')

    def act(self):
        if house.money < 50:
            self.work()
            house.total_money += 150
        if random.randint(1, 6) == 1 and self.satiety < 50:
            self.eat()
            house.total_food += 30
        elif random.randint(1, 6) == 2 and self.happiness < 50:
            self.play_the_game()
        elif random.randint(1, 6) == 4 and self.happiness < 50:
            self.pet_the_cat()

    def __str__(self):
        return f'{self.name} has {self.satiety} of satiety\n' \
               f'and has {self.happiness} of happiness.'


class Wife(HouseResident):
    def __init__(self, name, satiety=30, happiness=100):
        super().__init__(name, satiety, happiness)

    def __str__(self):
        return f'{self.name} has {self.satiety} of satiety\n' \
               f'and has {self.happiness} of happiness.'

    def go_to_the_shop(self):
        house.food += 100
        house.money -= 100
        self.satiety -= 10
        print(f'{self.name} go to the shop.')

    def buy_pet_food(self):
        house.money -= 50
        house.pet_food += 50
        self.satiety -= 10
        print(f'{self.name} buy pet food.')

    def pet_the_cat(self):
        self.happiness += 5
        self.satiety -= 10
        print(f'{self.name} pet the {Cat.__name__}.')

    def buy_the_coat(self):
        self.happiness += 60
        house.money -= 350
        self.satiety -= 10
        print(f'{self.name} buy the coat and very happy now.')

    def clean_the_house(self):
        self.satiety -= 10
        house.dirt -= 100
        if house.dirt < 0:
            house.dirt = 0
        print(f'{self.name} clean the house like Cinderella.')

    def act(self):
        if house.food < 30:
            self.go_to_the_shop()
            house.total_money += 100
        elif house.pet_food < 10:
            self.buy_pet_food()
            house.total_money += 50
        elif house.money > 400 and self.satiety < 30:
            self.buy_the_coat()
            house.total_money += 350
            house.total_coat_bought += 1
        elif random.randint(1, 3) == 3 and house.dirt > 50:
            self.clean_the_house()
        elif random.randint(1, 3) == 2 and self.satiety < 50:
            self.eat()
            house.total_food += 30
        elif random.randint(1, 3) == 1 and self.happiness < 50:
            self.pet_the_cat()


class Cat(HouseResident):

    def __init__(self, name, satiety=30):
        super().__init__(name, satiety)

    def __str__(self):
        return f'{self.name} has {self.satiety} of satiety.'

    def eat_pet_food(self):
        self.satiety += 20
        house.pet_food -= 10
        print(f'{self.name} eat pet food.')

    def scratch_wallpaper(self):
        house.dirt += 5
        self.satiety -= 10
        print(f'{self.name} has bad behavior and scratching the wallpaper.')

    def act(self):
        if self.satiety < 20:
            self.satiety += 20
        house.pet_food -= 10

        if random.randint(1, 3) == 1:
            self.scratch_wallpaper()
            house.dirt += 5
            self.satiety -= 10


class House:
    money = 100
    food = 50
    pet_food = 50
    dirt = 0
    total_money = 0
    total_food = 0
    total_coat_bought = 0

    def __init__(self, residents):
        self.residents = residents

    def __str__(self):
        return f'Family have {self.money} money.\n' \
               f'Family have {self.food} food.\n' \
               f'Cat has {self.pet_food} food\n' \
               f'Today is {self.dirt} level of dirt.'

    def one_day(self):
        for i_resident in self.residents:
            if house.dirt > 90:
                i_resident.happiness -= 20
                if isinstance(i_resident, Wife):
                    i_resident.clean_the_house()
            if i_resident.satiety < 30:
                i_resident.eat()
                house.total_food += 30
            i_resident.act()


my_family = []
father = Husband('George')
my_family.append(father)
mother = Wife('Bella')
my_family.append(mother)
pet = Cat('Lucius')
my_family.append(pet)
house = House(my_family)

for i_day in range(1, 366):
    print(f'\nIt is {i_day} day!\n')
    print(father)
    print(mother)
    print(pet)
    print(house)
    house.dirt += 5
    house.one_day()
print(f'Total information about one year of life:\n'
      f'Family has spent {house.total_money} of USD.\n'
      f'They have eaten {house.total_food} units of food.\n'
      f'They have bought {house.total_coat_bought} coats.')
