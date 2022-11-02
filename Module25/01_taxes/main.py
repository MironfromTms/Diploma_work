class Property:
    def __init__(self, worth):
        self.worth = worth

    def taxes(self):
        return 0


class Apartment(Property):
    def __init__(self, worth):
        super().__init__(worth)

    def taxes(self):
        taxes = self.worth * 1 / 1000
        return taxes


class Car(Property):
    def __init__(self, worth):
        super().__init__(worth)

    def taxes(self):
        taxes = self.worth * 1 / 200
        return taxes


class CountryHouse(Property):
    def __init__(self, worth):
        super().__init__(worth)

    def taxes(self):
        taxes = self.worth * 1 / 200
        return taxes


user_money = int(input('How much money do you have? '))
apartment_price = int(input('What price of your apartment? '))
car_price = int(input('What price of your car? '))
country_house_price = int(input('What price of your country house? '))
apartment = Apartment(apartment_price)
car = Car(car_price)
country_house = CountryHouse(country_house_price)
sum_of_taxes = apartment.taxes() + car.taxes() + country_house.taxes()
if user_money < sum_of_taxes:
    print('Dude! Your have not enough money to pay your taxes!')
else:
    print('It is ok! You can buy something else.')
