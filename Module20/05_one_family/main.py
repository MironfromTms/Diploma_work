# TODO здесь писать код
families = {('Сидоров', 'Никита'): 35,
            ('Сидорова', 'Алина'): 33,
            ('Сидоров', 'Павел'): 10,
            ('Иванов', 'Григорий'): 42,
            ('Иванова', 'Анна'): 39,
            ('Петров', 'Алесандр'): 33,
            ('Петрова', 'Алесандра'): 23,
            }

user_family = input('Введите фамилию: ')

for i_name, i_age in families.items():
    if user_family == i_name[0]:
        print(i_name[0], i_name[1], i_age)
    elif i_name[0][:-1] == user_family:
        print(i_name[0], i_name[1], i_age)
