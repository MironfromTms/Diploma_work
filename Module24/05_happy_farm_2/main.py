# TODO здесь писать код
class Potato:
    states = {0: 'Not planted', 1: 'Sprout', 2: 'Not enough ripe', 3: 'Has riped'}

    def __init__(self, index):
        self.index = index
        self.state = 0

    def grow(self):
        if self.state < 3:
            self.state += 1
        self.print_state()

    def is_ripe(self):
        if self.state == 3:
            return True
        return False

    def print_state(self):
        print('Potato {} now {}'.format(
            self.index, Potato.states[self.state]
        ))


class PotatoGarden:

    def __init__(self, count):
        self.potatoes = [Potato(index) for index in range(1, count + 1)]

    def grow_all(self):
        print('Potato is germinating!')
        for i_potato in self.potatoes:
            i_potato.grow()

    def are_all_ripe(self):
        for i_potato in self.potatoes:
            if not i_potato.is_ripe():
                print('Potato has not riped already!\n')
                return False
            else:
                print('All potato has riped. Please harvest!\n')
                return True


class Gardener:
    name = 'Billy Bob'

    def __init__(self, garden):
        self.garden = garden

    def water(self):
        print('Feed our garden with water.')
        self.garden.grow_all()

    def garden_care(self):
        if not my_garden.are_all_ripe():
            print('{} looking after the garden.\n'.format(self.name))
            return False
        else:
            print('Gardener is harvests.\n')
            return True


my_garden = PotatoGarden(5)
care = Gardener(my_garden)
for _ in range(3):
    my_garden.grow_all()
    my_garden.are_all_ripe()
    care.garden_care()
