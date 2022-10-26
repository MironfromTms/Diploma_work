# TODO здесь писать код
class Person:
    def __init__(self, name, surname, age):
        self.__name = name
        self.__surname = surname
        self.__age = age

    def get_name(self):
        return self.__name

    def get_surname(self):
        return self.__surname

    def get_age(self):
        return self.__age

    def set_age(self, value):
        if isinstance(value, (int, float)) and 0 <= value <= 100:
            self.__age = value
        else:
            raise ValueError("Age error!")

    def set_name(self, value):
        if isinstance(value, str) and value.isalpha():
            self.__name = value
        else:
            raise ValueError("Name error!")

    def set_surname(self, value):
        if isinstance(value, str) and value.isalpha():
            self.__surname = value
        else:
            raise ValueError("Surname error!")


class Employee(Person):
    def __init__(self, name, surname, age):
        super().__init__(name, surname, age)

    def salary(self):
        return 0


class Manager(Employee):
    salary = 13000

    def __init__(self, name, surname, age):
        super().__init__(name, surname, age)

    def __str__(self):
        return f'This is manager {self.get_name()} {self.get_surname()}\n' \
               f'Hi(Her) is {self.get_age()} years old\n' \
               f'His(Her) salary is {self.salary}\n'


class Agent(Employee):
    def __init__(self, name, surname, age, sales):
        super().__init__(name, surname, age)
        self.sales = sales

    def salary(self):
        return 5000 + self.sales * 0.05

    def __str__(self):
        return f'This is agent {self.get_name()} {self.get_surname()}\n' \
               f'Hi(Her) is {self.get_age()} years old\n' \
               f'His(Her) salary is {self.salary()}\n'


class Worker(Employee):
    def __init__(self, name, surname, age, hours):
        super().__init__(name, surname, age)
        self.hours = hours

    def salary(self):
        return 100 * self.hours

    def __str__(self):
        return f'This is manager {self.get_name()} {self.get_surname()}\n' \
               f'Hi(Her) is {self.get_age()} years old\n' \
               f'His(Her) salary is {self.salary()}\n'


employees_list = []
first_manage = Manager('Bob', 'Gilbert', 38)
employees_list.append(first_manage)
second_manager = Manager('Jane', 'Walker', 22)
employees_list.append(second_manager)
third_manager = Manager('Billy', 'Potter', 30)
employees_list.append(third_manager)
first_agent = Agent('Lily', 'Jobs', 27, 700000)
employees_list.append(first_agent)
second_agent = Agent('John', 'Godson', 42, 500000)
employees_list.append(second_agent)
third_agent = Agent('Jane', 'Turner', 19, 350000)
employees_list.append(third_agent)
first_worker = Worker('James', 'Gun', 44, 180)
employees_list.append(first_worker)
second_worker = Worker('Phill', 'King', 47, 167)
employees_list.append(second_worker)
third_worker = Worker('Steve', 'Oldman', 49, 190)
employees_list.append(third_worker)

list_of_salary = []
for i_employee in employees_list:
    print(i_employee.__str__())