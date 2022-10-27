import math


class Car:

    def __init__(self, x, y, angle):
        self.x = x
        self.y = y
        self.angle = angle

    def move(self, dist):
        self.x = self.x + dist * math.cos(self.angle)
        self.y = self.y + dist * math.sin(self.angle)


class Bus(Car):
    ticket_price = 0.1
    maximum_of_passengers = 45

    def __init__(self, x, y, direction):
        super().__init__(x, y, direction)
        self.passengers = 0
        self.money = 0

    def move(self, distance):
        self.money += self.ticket_price * self.passengers * distance
        super().move(distance)

    def take_the_passengers(self, passengers):
        if passengers + self.passengers > Bus.maximum_of_passengers:
            print('This bus is full now. Please wait for another one.')
        else:
            self.passengers += passengers
            print(f'{passengers} of passengers are come into the bus.')
        return passengers

    def get_off_the_passengers(self, passengers):
        if passengers > self.passengers:
            print('All people are get off from the bus.')
            self.passengers = 0
        else:
            self.passengers -= passengers
            print(f'{passengers} are get off from the bus.')


    def __str__(self):
        info = [
            f'In the bus now {self.passengers} passengers',
            f'The driver owned {round(self.money, 2)} USD',
        ]
        return '\n'.join(info)


bus = Bus(0, 0, 0)
bus.take_the_passengers(25)
bus.move(50)
print(bus)
bus.get_off_the_passengers(17)
print(bus)
bus.move(70)
bus.take_the_passengers(30)
print(bus)
bus.move(200)
bus.get_off_the_passengers(100)
print(bus)

