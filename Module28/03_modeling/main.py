from abc import ABC, abstractmethod


class Figure(ABC):
    def __init__(self, edge, height, base) -> None:
        self.edge = edge
        self.height = height
        self.base = base

    @property
    def edge(self) -> int:
        return self._edge

    @edge.setter
    def edge(self, value: int) -> None:
        self._edge = value

    @property
    def height(self) -> int:
        return self._height

    @height.setter
    def height(self, value: int) -> None:
        self._height = value

    @property
    def base(self) -> int:
        return self._base

    @base.setter
    def base(self, value: int) -> None:
        self._base = value

    @abstractmethod
    def area(self) -> None:
        pass

    @abstractmethod
    def perimetr(self) -> None:
        pass


class Triangle(Figure):
    def __init__(self, edge: int, height: int, base: int):
        super().__init__(edge, height, base)
        self.edge = edge
        self.height = height
        self.base = base

    def perimetr(self) -> int:
        return self.base + self.edge * 2

    def area(self):
        return self.edge * self.base / 2


class Square(Figure):
    def __init__(self, edge: int) -> None:
        super().__init__(edge, None, None)

    def perimetr(self) -> int:
        return self.edge * 4

    def area(self) -> int:
        return (self.edge ** 2) * 6


class Cube(Square):

    def surface_area(self):
        return 6 * self.edge ** 2


class Pyramid(Triangle):
    def surface_area(self):
        return self.base ** 2 + 4 * self.base * self.edge / 2


square = Square(5)
triangle = Triangle(5, 4, 8)
cube = Cube(6)
pyramid = Pyramid(6, 5, 8)
print(square.perimetr(), square.area())
print(triangle.perimetr(), triangle.area())
print(cube.surface_area())
print(pyramid.surface_area())
