import random


class HouseResident:
    def __init__(self, name, satiety, happiness=None):
        self.name = name
        self.satiety = satiety
        self.happiness = happiness

    def eat(self):
        House.food -= 30
        self.satiety += 30
        print(f'{self.name} is eating.')


class Husband(HouseResident):
    def __init__(self, name, satiety=30, happiness=100):
        super().__init__(name, satiety, happiness)

    def work(self):
        House.money += 150
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
        House.food += 100
        House.money -= 100
        self.satiety -= 10
        print(f'{self.name} go to the shop.')

    def buy_pet_food(self):
        House.money -= 50
        House.pet_food += 50
        self.satiety -= 10
        print(f'{self.name} buy pet food.')

    def pet_the_cat(self):
        self.happiness += 5
        self.satiety -= 10
        print(f'{self.name} pet the {Cat.__name__}.')

    def buy_the_coat(self):
        self.happiness += 60
        House.money -= 350
        self.satiety -= 10
        print(f'{self.name} buy the coat and very happy now.')

    def clean_the_house(self):
        self.satiety -= 10
        House.dirt -= 100
        print(f'{self.name} clean the house like Cinderella.')


class Cat(HouseResident):

    def __init__(self, name, satiety=30):
        super().__init__(name, satiety)

    def __str__(self):
        return f'{self.name} has {self.satiety} of satiety.'

    def eat_pet_food(self):
        self.satiety += 20
        House.pet_food -= 10
        print(f'{self.name} eat pet food.')

    def scratch_wallpaper(self):
        House.dirt += 5
        self.satiety -= 10
        print(f'{self.name} has bad behavior and scratching the wallpaper.')


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
            if House.dirt > 90:
                i_resident.happiness -= 20
                if isinstance(i_resident, Wife):
                    i_resident.clean_the_house()
            if i_resident.satiety < 30:
                i_resident.eat()
                House.total_food += 30
            elif isinstance(i_resident, Cat) and i_resident.satiety < 20:
                i_resident.satiety += 20
                House.pet_food -= 10
            elif isinstance(i_resident, Cat):
                if random.randint(1, 3) == 1:
                    i_resident.scratch_wallpaper()
                    House.dirt += 5
                    i_resident.satiety -= 10
            elif isinstance(i_resident, Wife):
                if House.food < 30:
                    i_resident.go_to_the_shop()
                    House.total_money += 100
                elif House.pet_food < 10:
                    i_resident.buy_pet_food()
                    House.total_money += 50
                elif House.money > 400 and i_resident.satiety < 30:
                    i_resident.buy_the_coat()
                    House.total_money += 350
                    House.total_coat_bought += 1
                elif random.randint(1, 3) == 3 and House.dirt > 50:
                    i_resident.clean_the_house()
                elif random.randint(1, 3) == 2 and i_resident.satiety < 50:
                    i_resident.eat()
                    House.total_food += 30
                elif random.randint(1, 3) == 1 and i_resident.happiness < 50:
                    i_resident.pet_the_cat()
            elif isinstance(i_resident, Husband):
                if House.money < 50:
                    i_resident.work()
                    House.total_money += 150
                    break
                if random.randint(1, 6) == 1 and i_resident.satiety < 50:
                    i_resident.eat()
                    House.total_food += 30
                elif random.randint(1, 6) == 2 and i_resident.happiness < 50:
                    i_resident.play_the_game()
                elif random.randint(1, 6) == 4 and i_resident.happiness < 50:
                    i_resident.pet_the_cat()


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
    House.dirt += 5
    house.one_day()
print(f'Total information about one year of life:\n'
      f'Family has spent {House.total_money} of USD.\n'
      f'They have eaten {House.total_food} units of food.\n'
      f'They have bought {House.total_coat_bought} coats.')
