# TODO здесь писать код
# Вот таблица преобразований:
# Вода + Воздух = Шторм
# Вода + Огонь = Пар
# Вода + Земля = Грязь
# Воздух + Огонь = Молния
# Воздух + Земля = Пыль
# Огонь + Земля = Лава


class Water:
    def __str__(self):
        return 'Water'

    def __add__(self, other):
        if isinstance(other, Air):
            return Storm()
        elif isinstance(other, Fire):
            return Steam()
        elif isinstance(other, Earth):
            return Dirt()
        else:
            return None


class Fire:
    def __str__(self):
        return 'Fire'

    def __add__(self, other):
        if isinstance(other, Water):
            return Steam()
        elif isinstance(other, Earth):
            return Lava()
        elif isinstance(other, Air):
            return Lightning()
        else:
            return None


class Earth:
    def __str__(self):
        return 'Earth'

    def __add__(self, other):
        if isinstance(other, Fire):
            return Lava()
        elif isinstance(other, Water):
            return Dirt()
        elif isinstance(other, Air):
            return Air()
        else:
            return None


class Air:
    def __str__(self):
        return 'Air'

    def __add__(self, other):
        if isinstance(other, Water):
            return Storm()
        elif isinstance(other, Fire):
            return Lightning()
        elif isinstance(other, Earth):
            return Dust()
        else:
            return None


class Storm:
    def __str__(self):
        return 'Storm'


class Steam:
    def __str__(self):
        return 'Steam'


class Dirt:
    def __str__(self):
        return 'Dirt'


class Lightning:
    def __str__(self):
        return 'Lightning'


class Dust:
    def __str__(self):
        return 'Dust'


class Lava:
    def __str__(self):
        return 'Lava'


water = Water()
air = Air()
fire = Fire()
earth = Earth()
dust = air + earth
lightning = air + fire
storm = water + air
dirt = water + earth
steam = water + fire
lava = fire + earth
print(storm)
print(dirt)
print(steam)
print(lava)
