class MyMath:
    radius = 0
    cube_edge = 0

    @classmethod
    def circle_len(cls, radius: int) -> float:
        cls.radius = radius
        return round((cls.radius * 2 * 3.14), 2)

    @classmethod
    def circle_sq(cls, radius: int) -> float:
        cls.radius = radius
        return round((3.14 * cls.radius ** 2), 2)

    @classmethod
    def cube_sq(cls, cube_edge: int) -> int:
        cls.cube_edge = cube_edge
        return cube_edge ** 3

    @classmethod
    def sphere_sq(cls, radius: int) -> float:
        cls.radius = radius
        return round((4 * 3.14 * cls.radius ** 2), 2)


res_1 = MyMath.circle_len(radius=5)
print(res_1)
res_2 = MyMath.circle_sq(radius=6)
print(res_2)
res_3 = MyMath.cube_sq(5)
print(res_3)
res_4 = MyMath.sphere_sq(6)
print(res_4)
