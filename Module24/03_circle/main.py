# TODO здесь писать код
class Circle:
    def __init__(self, x=0, y=0, radius=1):
        self.x = x
        self.y = y
        self.radius = radius

    def square(self):
        return 3.14 * self.radius ** 2

    def perimetr(self):
        return 2 * 3.14 * self.radius

    def get_bigger(self, k):
        self.radius *= k

    def is_intersect(self, second_circle):
        distance_between_centers = ((second_circle.y - self.y) ** 2 + (second_circle.x - self.x) ** 2) ** 0.5
        print(distance_between_centers)
        sum_of_radiuses = self.radius + second_circle.radius
        print(sum_of_radiuses)
        if distance_between_centers < sum_of_radiuses:
            print('This circles are intersecting')
        else:
            print('This circles are not intersecting')


first_circle = Circle(x=1, y=2, radius=2)
second_circle = Circle(x=5, y=9, radius=3)
first_circle.is_intersect(second_circle)
