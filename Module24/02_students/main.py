students = [['Petr Ivanov', 4402, [3, 2, 3, 4, 5]],
            ['Ivan Petrov', 4402, [3, 5, 3, 4, 5]],
            ['Denis Petrov', 4401, [3, 5, 5, 4, 5]],
            ['Sergey Petrov', 4402, [3, 5, 3, 5, 5]],
            ['Ivan Sergeev', 4402, [3, 5, 3, 4, 5]],
            ['Ivan Denisov', 4402, [3, 5, 5, 5, 5]],
            ['Dmirii Petrov', 4402, [3, 4, 4, 4, 5]],
            ['Ivan Dmitrov', 4402, [3, 5, 4, 4, 4]],
            ['Iurii Petrov', 4402, [4, 4, 4, 4, 4]],
            ['Ivan Iuriev', 4402, [5, 5, 5, 4, 5]]]


def avr_of_list(student):
    avr = sum(student.graduates) / len(student.graduates)
    return avr


class Student:

    def __init__(self, surname, group_number, graduates):
        self.surname = surname
        self.group_number = group_number
        self.graduates = graduates

    def print_info(self):
        print(f'Student {self.surname} from group {self.group_number} has maks: {self.graduates}')


students_list = []
for i in range(10):
    i_student = Student(surname=students[i][0], group_number=students[i][1], graduates=students[i][2])
    students_list.append(i_student)
students_list.sort(key=avr_of_list)
for i_student in students_list:
    i_student.print_info()