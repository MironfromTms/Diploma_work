# TODO здесь писать код
class Parent:
    def __init__(self, name, age, children_list):
        self.name = name
        self.age = age
        self.children_list = children_list

    def self_info(self):
        children_str = ', '.join(self.children_list)
        print(f'Hi! My name is {self.name}.'
              f' I am {self.age} years old.\n'
              f'I have {len(self.children_list)} children.'
              f' There names are : {children_str}\n')

    def calm_down_the_kid(self, Children):
        if Children.name not in self.children_list:
            print(f'{Children.name} is not your kid!')
        elif self.age - Children.age < 16:
            print(f'{Children.name} not a kid, man! ')
        else:
            if not Children.calm:
                print(f'{Children.name} not calm down! Please help us!')
                first_kid.calm = True
                print(f'{Children.name} now is calm down!')
            else:
                print(f'{Children.name} has already calmed down!')

    def feed_the_kid(self, Children):
        if Children.name not in self.children_list:
            print(f'{Children.name} is not your kid!')
        elif self.age - Children.age < 16:
            print(f'{Children.name} not a kid, man! ')
        else:
            if Children.hungry:
                print(f'{Children.name} is hungry! Please feed the kid!')
                Children.hungry = False
                print(f'{Children.name} is fed!')
            else:
                print(f'{Children.name} is not hungry')


class Child:
    def __init__(self, name, age, calm=True, hungry=True):
        self.name = name
        self.age = age
        self.calm = calm
        self.hungry = hungry


first_parent = Parent('Bob', 44, ['Amy', 'Billy', 'Jerry'])
first_parent.self_info()
first_kid = Child('Amy', 10, calm=False, hungry=True)
second_kid = Child('Billy', 6, calm=True, hungry=True)
third_kid = Child('Jerry', 20, calm=False, hungry=False)
fourth_kid = Child('Jimmy', 30, calm=False, hungry=True)
fifth_kid = Child('Amy', 36, calm=False, hungry=True)
first_parent.feed_the_kid(first_kid)
first_parent.feed_the_kid(fourth_kid)
first_parent.calm_down_the_kid(second_kid)
first_parent.calm_down_the_kid(third_kid)
first_parent.feed_the_kid(fifth_kid)